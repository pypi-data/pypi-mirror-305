import os
import unittest
import atooms.trajectory as trj
import berni
try:
    import rumd
    import berni.rumd
    from atooms.backends.rumd import RUMD
    SKIP = False
except ImportError:
    SKIP = True

class Test(unittest.TestCase):

    def setUp(self):
        if SKIP:
            self.skipTest('missing RUMD')
        self.root = os.path.dirname(__file__)

    def test_(self):
        for model in ['kob_andersen', 'coslovich_pastore']:
            pot = berni.rumd.potential(model)

    def test_cp(self):
        import berni
        inp = berni.samples.get('coslovich_pastore-488db481cdac35e599922a26129c3e35.xyz')
        trj.TrajectoryXYZ(inp).copy(cls=trj.TrajectoryRUMD, fout='/tmp/1.xyz')
        model = 'coslovich_pastore'
        potentials = berni.rumd.potential(model)
        backend = RUMD('/tmp/1.xyz', potentials=potentials)
        epot_0 = backend.system.potential_energy(per_particle=True)

        model = 'coslovich_pastore'
        model = berni.get(model)
        model['cutoff'][0]['type'] = 'linear_cut_shift'
        model['cutoff'][0]['parameters']['rcut'] = model['cutoff'][0]['parameters']['rspl']
        model['cutoff'][0]['parameters'].pop('rspl')
        with trj.Trajectory(inp) as th:
            s = th[0]
            s.species_layout = 'F'
            s.interaction = berni.f90.Interaction(model)
            epot_1 = s.potential_energy(per_particle=True)
        self.assertLess(abs(epot_0 - epot_1), 1e-6)
        import os
        os.system(f'rm -f {inp}')

    def test_ka(self):
        inp = berni.samples.get('kob_andersen-8f4a9fe755e5c1966c10b50c9a53e6bf.xyz')
        trj.TrajectoryXYZ(inp).copy(cls=trj.TrajectoryRUMD, fout='/tmp/1.xyz')
        model = 'kob_andersen'
        potentials = berni.rumd.potential(model)
        backend = RUMD('/tmp/1.xyz', potentials=potentials)
        epot_0 = backend.system.potential_energy(per_particle=True)
        model = 'kob_andersen'
        with trj.Trajectory(inp) as th:
            s = th[0]
            s.species_layout = 'F'
            s.interaction = berni.f90.Interaction(model)
            epot_1 = s.potential_energy(per_particle=True)
        self.assertLess(abs(epot_0 - epot_1), 1e-6)
        import os
        os.system(f'rm -f {inp}')

    def tearDown(self):
        import os
        os.system('rm -f /tmp/1.xyz')


class TestLAMMPS(unittest.TestCase):

    def _system(self, fname):
        with trj.Trajectory(fname) as th:
            system = th[0]
        system.species_layout = 'F'
        return system

    def _backends(self, system, model):
        import atooms.backends.lammps
        import atooms.backends.f90
        import berni.lammps
        import berni.f90
        # LAMMPS
        cmd = berni.lammps.export(model)
        system.interaction = atooms.backends.lammps.Interaction(cmd)
        epot_lammps = system.potential_energy(per_particle=True)

        # LAMMPS tabulated
        cmd = berni.lammps.export(model, tabulate=True)
        system.interaction = atooms.backends.lammps.Interaction(cmd)
        epot_lammps_tab = system.potential_energy(per_particle=True)
        # Atooms
        system.interaction = atooms.backends.f90.Interaction(model)
        epot_f90 = system.potential_energy(per_particle=True)

        self.assertAlmostEqual(epot_lammps, epot_f90)
        self.assertAlmostEqual(epot_lammps, epot_lammps_tab)
        # print(epot_lammps, epot_lammps_tab)

    def _supported(self, system, model, backend):
        import atooms.backends.lammps
        import atooms.backends.f90
        import berni.lammps
        import berni.f90
        if backend == 'lammps':
            cmd = berni.lammps.export(model)
            system.interaction = atooms.backends.lammps.Interaction(cmd)
            epot_lammps = system.potential_energy(per_particle=True)
        if backend == 'f90':
            system.interaction = atooms.backends.f90.Interaction(model)
            epot_f90 = system.potential_energy(per_particle=True)

    def test_lj(self):
        model = berni.get("lennard_jones")
        fname = berni.samples.get("lennard_jones-13ce47602b259f7802e89e23ffd57f19.xyz")
        system = self._system(fname)
        self._backends(system, model)

    def test_ka(self):
        model = berni.models.get('kob_andersen')
        fname = berni.samples.get('kob_andersen-8f4a9fe755e5c1966c10b50c9a53e6bf.xyz')
        system = self._system(fname)
        self._backends(system, model)

    def _backend_support(self, backend):
        """Test all potentials"""
        import inspect
        fname = berni.samples.get("lennard_jones-13ce47602b259f7802e89e23ffd57f19.xyz")
        system = self._system(fname)
        ignore = {
            'f90': ['fene'],
            'lammps': ['fene']
        }
        unsupported, supported = [], []
        for phi, func in berni.potentials.items():
            if phi in ignore['f90']:
                continue

            args = func.__code__.co_varnames[1:]
            args = inspect.getfullargspec(func)[0]
            defaults = inspect.getfullargspec(func)[3]
            params = {arg: [[default]] for arg, default in zip(args[1:], defaults)}

            model = {
                'potential': [{
                    'type': phi,
                    'parameters': params
                }
                ],
                'cutoff': [{
                    'type': 'cut_shift',
                    'parameters': {'rcut': [[2.5]]}
                }
                ]
            }
            # if phi != 'yukawa': continue
            # print(phi)
            # print(model)
            # self._supported(system, model, backend)
            try:
                self._supported(system, model, backend)
                supported.append(phi)
            except:
                unsupported.append(phi)
        return supported, unsupported

    def test_support_f90(self):
        # print('{} {}'.format(*zip(['YES', 'NO'], self._backend_support('f90'))))
        self._backend_support('f90')

    def test_support_lammps(self):
        # print('{} {}'.format(*zip(['YES', 'NO'], self._backend_support('lammps'))))
        self._backend_support('lammps')


if __name__ == '__main__':
    unittest.main()
