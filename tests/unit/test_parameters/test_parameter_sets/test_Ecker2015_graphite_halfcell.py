#
# Tests for O'Kane (2022) parameter set
#
from tests import TestCase
import pybamm
import unittest


class TestEcker2015_graphite_halfcell(TestCase):
    def test_functions(self):
        param = pybamm.ParameterValues("Ecker2015_graphite_halfcell")
        sto = pybamm.Scalar(0.5)
        T = pybamm.Scalar(298.15)

        fun_test = {
            # Positive electrode
            "Positive electrode diffusivity [m2.s-1]": ([sto, T], 1.219e-14),
            "Positive electrode exchange-current density [A.m-2]": (
                [1000, 15960, 31920, T],
                6.2517,
            ),
            "Positive electrode OCP [V]": ([sto], 0.124),
            # Electrolyte
            "Electrolyte diffusivity [m2.s-1]": ([1000, T], 2.593e-10),
            "Electrolyte conductivity [S.m-1]": ([1000, T], 0.9738),
        }

        for name, value in fun_test.items():
            self.assertAlmostEqual(
                param.evaluate(param[name](*value[0])), value[1], places=4
            )


if __name__ == "__main__":
    print("Add -v for more debug output")
    import sys

    if "-v" in sys.argv:
        debug = True
    pybamm.settings.debug_mode = True
    unittest.main()
