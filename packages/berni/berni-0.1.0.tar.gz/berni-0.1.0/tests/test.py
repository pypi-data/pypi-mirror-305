#!/usr/bin/env python

import os
import unittest
from berni import models, samples, schema

root = os.path.dirname(__file__)

class Test(unittest.TestCase):

    def setUp(self):
        pass

    def _compare_data(self, ref, copy):
        with open(ref) as fh:
            data = fh.read()
        with open(copy) as fh:
            data_copy = fh.read()
        self.assertEqual(data, data_copy)

    def test_grammar(self):
        models.all()
        models.get("lennard_jones")
        samples.all()
        samples.get("lennard_jones-5cc3b80bc415fa5c262e83410ca65779.xyz")

    def test(self):
        sample = samples.get("lennard_jones-5cc3b80bc415fa5c262e83410ca65779.xyz")
        raw = root + '/../berni/samples/lennard_jones-5cc3b80bc415fa5c262e83410ca65779.xyz'
        self._compare_data(raw, sample)

    def test_convert(self):
        m = {
            "metadata": {'name': 'lj'},
            "potential": [
                {
                    "type": "lennard_jones",
                    "parameters": {"sigma": [[1.0, 0.8], [0.8, 0.88]],
                                   "epsilon": [[1.0, 1.5], [1.5, 0.5]]}
                }
            ],
            "cutoff": [
                {
                    "type": "cut_shift",
                    "parameters": {"rcut": [[2.5, 2.0], [2.0, 2.2]]}
                }
            ]
        }
        n = {'potential': [{'cutoff': {'parameters': {'1-1': {'rcut': 2.5},
                                                      '1-2': {'rcut': 2.0},
                                                      '2-2': {'rcut': 2.2}},
                                       'type': 'cut_shift'},
                            'parameters': {'1-1': {'epsilon': 1.0, 'sigma': 1.0},
                                           '1-2': {'epsilon': 1.5, 'sigma': 0.8},
                                           '2-2': {'epsilon': 0.5, 'sigma': 0.88}},
                            'type': 'lennard_jones'}],
             "metadata": {'name': 'lj'},
             }
        self.assertEqual(m, schema._convert(m, 1))
        self.assertEqual(n, schema._convert(m, 2))

    def test_schemas(self):
        from jsonschema import validate
        from berni import models

        for version in [1, ]:
            models.default_table_name = version
            for model in models:
                # Moving the payload to _model means that we cannot
                # use model right away, we must get it
                validate(instance=models.get(model['name']),
                         schema=schema.schemas[version])

    def test_storage(self):
        import glob
        from berni import Query
        query = Query()
        sample = samples.search((query.model == 'lennard_jones') &
                                (query.density == 1.0))[0]
        name = sample['name']
        self.assertTrue(len(samples.get(name)) > 0)

    def test_pprint(self):
        with open('/dev/null', 'w') as null:
            models.pprint(file=null)
            models.pprint(include=['name', 'doi'], file=null)

    def test_potentials(self):
        from berni import potentials
        for f in potentials.values():
            f(0.9)

    def test_tabulate(self):
        from berni.helpers import tabulate
        from berni import potentials, cutoffs

        func = potentials['lennard_jones']
        # print(out)
        # print(func(1.0))
        # cutoff = cutoffs['shift'](func, params={}, cutoff_params={'rcut': [[2.5]]})
        cutoff = cutoffs['shift'](func, params={}, cutoff_params={'rcut': 2.5})
        cut_func = cutoff(func)
        self.assertAlmostEqual(cut_func(1.0)[0], func(1.0)[0] - func(2.5)[0])
        # print(dir(cut_func))
        # print(func(1.0))
        # print(func(1.0)[0])
        # print(cut_func(1.0)[0])
        # print(func(2.5)[0], cut_func(2.5)[0])
        out = tabulate(cut_func, rmax=cut_func._params['rcut'], npoints=100, overshoot=0)
        # print(out[0][-4]**0.5, out[1][-4])
        # print(out[0][-3]**0.5, out[1][-3])
        # print(out[0][-2]**0.5, out[1][-2])
        self.assertAlmostEqual(out[0][-1]**0.5, 2.5)
        self.assertAlmostEqual(out[1][-1], 0.0)

    def test_tabulate_lammps(self):
        import berni.lammps
        from berni import potentials, cutoffs

        func = potentials['lennard_jones']
        cutoff = cutoffs['shift'](func, params={}, cutoff_params={'rcut': 2.5})
        func = cutoff(func)
        out = berni.lammps._tabulate_lammps(func, rmin=0.0, npoints=1000,
                                            overshoot=0)

        model = berni.model('kob_andersen')
        cmd = berni.lammps._tabulate(model)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
