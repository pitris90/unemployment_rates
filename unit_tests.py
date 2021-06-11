# Unit Tests
# NOTE: Test with included json file

from unemployment import rates_from_year, lowest_countries, highest_countries\
    , load_json
import sys
import io

rates2003 = [5.943826289, 4.278559338, 8.158333333, 7.594616751, 9.5433848,
             7.818066527, 5.344516646, 10.03010116, 9.017860131, 8.503978378,
             9.134738857, 9.712526535, 5.860132523, 3.352836045, 4.739670964,
             13.28016732, 8.444973801, 5.25125, 3.562065618, 3.304883869,
             2.998805894, 3.975713818, 4.76074516, 4.04172726, 19.61702787,
             6.276549712, 17.55389647, 6.682102697, 11.03816292, 6.56574156,
             4.033356027, 10.82310834, 5.019884066, 5.986539203, 8.68886389,
             6.971079892]

rates2004 = [5.39663128, 4.939707755, 8.4, 7.167833951, 10.00149582,
             8.323638425, 5.516904324, 9.661753538, 8.80435787, 8.8650811,
             9.829230121, 10.49281197, 6.096400087, 3.06335905, 4.539966682,
             12.85704871, 7.996760207, 4.717099486, 3.67219364, 3.710506994,
             3.695332444, 4.894207123, 4.018968583, 4.186831741, 18.97466246,
             6.666642728, 18.22108629, 6.291982582, 10.54622939, 7.373480411,
             4.31699694, 10.58802629, 4.768990278, 5.523039996, 8.942669403,
             6.859814025]

rates2005 = [5.044790587, 5.152160612, 8.483333333, 6.748691501, 9.224422554,
             7.922330988, 4.793715416, 7.899232972, 8.368797468, 8.882978134,
             10.69442137, 9.849833119, 7.185491402, 2.590345651, 4.341850838,
             11.29834866, 7.708360512, 4.424423923, 3.734708533, 4.099797561,
             3.540173119, 5.113659881, 3.807106599, 4.382939676, 17.74593227,
             7.597516675, 16.25634386, 6.516689478, 9.156961086, 7.652096974,
             4.329724566, 10.40296232, 4.852538715, 5.076780521, 8.941482912,
             6.629153129]

rates2006 = [4.789362794, 4.727182858, 8.266666667, 6.307841105, 7.773166282,
             7.142271671, 3.868296418, 5.905173373, 7.702632855, 8.835277292,
             9.694756306, 8.890878396, 7.451740837, 2.878830234, 4.415526325,
             10.47596715, 6.777043598, 4.129376275, 3.450431799, 4.242014975,
             3.550553518, 4.20994586, 3.840522581, 3.392420144, 13.84039072,
             7.637987286, 13.3725907, 5.945157013, 8.511101588, 7.053667613,
             3.941659077, 10.01247258, 5.450636437, 4.617465075, 8.233837469,
             6.100565063]

rates2007 = [4.379649386, 4.399730726, 7.466666667, 6.049842626, 7.150623348,
             5.316363283, 3.669496447, 4.659913473, 6.850344695, 8.009145174,
             8.310233377, 8.276300402, 7.35706148, 2.301867378, 4.571302023,
             9.147672881, 6.110290905, 3.84841253, 3.233335111, 4.182611437,
             3.672170595, 3.475695941, 3.655294639, 2.498729296, 9.601554043,
             7.99012509, 11.14262294, 4.816202781, 8.264570818, 6.127066505,
             3.57509152, 10.06182773, 5.355104552, 4.619105436, 7.409607055,
             5.656171098]

rates2008 = [4.249093453, 3.813933625, 7.016666667, 6.146014664, 7.787221805,
             4.391669598, 3.326692683, 5.601684952, 6.368216471, 7.384897537,
             7.188163108, 7.653084476, 7.851089777, 2.990597714, 6.024123088,
             7.728344307, 6.774113796, 3.979750388, 3.15974989, 4.14500326,
             3.949416134, 3.018534226, 4.160280272, 2.565344859, 7.117494731,
             7.607584033, 9.507520125, 4.368899066, 11.33829871, 6.183935584,
             3.341272685, 10.74264555, 5.708223236, 5.800444743, 7.436710115,
             5.982685271]

rates2009 = [5.592226603, 4.776912506, 7.891892855, 8.284689299, 10.80236438,
             6.675050668, 5.821647379, 13.87805579, 8.269856093, 9.129199553,
             7.429105355, 9.460314273, 10.0153875, 7.241470693, 11.81229736,
             9.476560711, 7.800833899, 5.068375853, 3.643064158, 5.431987487,
             5.43621902, 3.68444758, 6.146341463, 3.107969091, 8.166610723,
             9.484363464, 12.02516939, 5.856004508, 18.01195661, 8.305635992,
             4.257833072, 13.74762357, 7.62507775, 9.275245924, 9.371745367,
             8.157564657]

rates2010 = [5.230660289, 4.391591645, 8.283171959, 7.988900419, 8.121579077,
             7.273107122, 7.191696186, 16.83438817, 8.381534292, 9.315864403,
             6.757338631, 12.53058153, 11.14448405, 7.55861225, 13.62078809,
             8.33683595, 8.41234985, 5.058985674, 3.715763348, 5.778771292,
             5.373117407, 4.383579198, 6.537348623, 3.521797592, 9.622661542,
             10.81324061, 14.37913326, 7.240345922, 20.06321219, 8.372715009,
             4.44955058, 11.65601928, 7.861627732, 9.627692959, 9.891824566,
             8.320563893]

rates2011 = [5.099422942, 4.143587245, 7.175138783, 7.453609598, 7.104778251,
             6.723482523, 7.313112408, 12.4576855, 7.774845319, 9.202432489,
             5.752587233, 17.65238747, 10.92071597, 7.058807671, 14.51224844,
             7.110513831, 8.438703909, 4.592622773, 3.405129308, 5.627283477,
             5.240905522, 4.343866431, 6.509125435, 3.212318473, 9.648757987,
             12.7097409, 13.54138898, 8.164977774, 21.63712759, 7.504247076,
             3.949110999, 9.605142332, 8.078635307, 8.94612643, 9.978460373,
             7.953121271]

rates2012 = [5.224336088, 4.351345785, 7.381153404, 7.32358421, 6.477468723,
             6.936394665, 7.544640558, 9.873121257, 7.722836877, 9.877166456,
             5.28775372, 23.5737508, 11.12538821, 6.138731401, 14.79227286,
             6.8731402, 10.55546863, 4.399496241, 3.378067785, 6.078760003,
             5.036393758, 5.163411369, 6.938443309, 3.098584692, 10.05073744,
             15.52457602, 13.69591839, 8.529917685, 25.04773498, 7.651519753,
             3.863659425, 9.014001387, 8.027613742, 8.091574662, 11.11907575,
             7.970392182]

rates2013 = [5.50415003, 4.695491708, 7.689552898, 7.169741525, 6.78101031,
             7.242148075, 7.357364231, 9.116309666, 7.962718148, 10.66140443,
             5.524081118, 26.6534591, 11.09958634, 5.393148124, 14.73886731,
             7.359377644, 11.42167502, 4.355894653, 3.618601827, 6.589474092,
             4.990182757, 5.801548283, 6.568824155, 3.098584692, 10.49463234,
             16.93137173, 13.5763623, 9.708595873, 26.89014696, 7.912693788,
             4.109877511, 9.320782097, 8.275155581, 7.810715126, 11.9135905,
             8.15379125]

rates2014 = [5.462866231, 4.745323313, 7.735442636, 6.88122705, 6.780198936,
             7.135151601, 7.255659852, 8.74566981, 7.757742455, 10.91985917,
             5.565600014, 27.2364419, 10.76358386, 5.128315309, 14.61076214,
             6.93094611, 11.7584873, 4.286733019, 3.397535556, 6.658818611,
             4.897580596, 6.10348765, 6.048820957, 3.003021166, 10.66450371,
             16.62982306, 12.97187212, 9.847243093, 26.78073067, 7.604124855,
             3.999499419, 8.651402638, 8.036560522, 7.514930043, 11.99849464,
             8.004598637]

lowest_countries2003 = "3 countries with lowest unemployment rates:" \
                       "\nMexico\nLuxembourg\nIceland\n"

lowest_countries2004 = "3 countries with lowest unemployment rates:" \
                       "\nIceland\nKorea\nMexico\n"

lowest_countries2005 = "3 countries with lowest unemployment rates:" \
                       "\nIceland\nMexico\nKorea\n"

lowest_countries2006 = "3 countries with lowest unemployment rates:" \
                       "\nIceland\nNorway\nKorea\n"

lowest_countries2007 = "3 countries with lowest unemployment rates:" \
                       "\nIceland\nNorway\nKorea\n"

lowest_countries2008 = "3 countries with lowest unemployment rates:" \
                       "\nNorway\nIceland\nNetherlands\n"

lowest_countries2009 = "3 countries with lowest unemployment rates:" \
                       "\nNorway\nKorea\nNetherlands\n"

lowest_countries2010 = "3 countries with lowest unemployment rates:" \
                       "\nNorway\nKorea\nNetherlands\n"

lowest_countries2011 = "3 countries with lowest unemployment rates:" \
                       "\nNorway\nKorea\nSwitzerland\n"

lowest_countries2012 = "3 countries with lowest unemployment rates:" \
                       "\nNorway\nKorea\nSwitzerland\n"

lowest_countries2013 = "3 countries with lowest unemployment rates:" \
                       "\nNorway\nKorea\nSwitzerland\n"

lowest_countries2014 = "3 countries with lowest unemployment rates:" \
                       "\nNorway\nKorea\nSwitzerland\n"

highest_countries2003 = "3 countries with highest unemployment rates:" \
                        "\nPoland\nSlovak Republic\nIsrael\n"

highest_countries2004 = "3 countries with highest unemployment rates:" \
                        "\nPoland\nSlovak Republic\nIsrael\n"

highest_countries2005 = "3 countries with highest unemployment rates:" \
                        "\nPoland\nSlovak Republic\nIsrael\n"

highest_countries2006 = "3 countries with highest unemployment rates:" \
                        "\nPoland\nSlovak Republic\nIsrael\n"

highest_countries2007 = "3 countries with highest unemployment rates:" \
                        "\nSlovak Republic\nTurkey\nPoland\n"

highest_countries2008 = "3 countries with highest unemployment rates:" \
                        "\nSpain\nTurkey\nSlovak Republic\n"

highest_countries2009 = "3 countries with highest unemployment rates:" \
                        "\nSpain\nEstonia\nTurkey\n"

highest_countries2010 = "3 countries with highest unemployment rates:" \
                        "\nSpain\nEstonia\nSlovak Republic\n"

highest_countries2011 = "3 countries with highest unemployment rates:" \
                        "\nSpain\nGreece\nIreland\n"

highest_countries2012 = "3 countries with highest unemployment rates:" \
                        "\nSpain\nGreece\nPortugal\n"

highest_countries2013 = "3 countries with highest unemployment rates:" \
                        "\nSpain\nGreece\nPortugal\n"

highest_countries2014 = "3 countries with highest unemployment rates:" \
                        "\nGreece\nSpain\nPortugal\n"


rates = [rates2003, rates2004, rates2005, rates2006, rates2007, rates2008,
         rates2009, rates2010, rates2011, rates2012, rates2013, rates2014]

lowest = [lowest_countries2003, lowest_countries2004, lowest_countries2005,
          lowest_countries2006, lowest_countries2007, lowest_countries2008,
          lowest_countries2009, lowest_countries2010, lowest_countries2011,
          lowest_countries2012, lowest_countries2013, lowest_countries2014]

highest = [highest_countries2003, highest_countries2004, highest_countries2005,
           highest_countries2006, highest_countries2007, highest_countries2008,
           highest_countries2009, highest_countries2010, highest_countries2011,
           highest_countries2012, highest_countries2013, highest_countries2014]

loaded = load_json()


def test_rates_from_year():
    for i in range(12):
        assert rates_from_year(loaded, i + 2003) == rates[i]


def test_lowest_countries():
    for i in range(12):
        captured = io.StringIO()
        sys.stdout = captured
        lowest_countries(loaded, rates_from_year(loaded, i + 2003), 3)
        sys.stdout = sys.__stdout__
        assert captured.getvalue() == lowest[i]


def test_highest_countries():
    for i in range(12):
        captured = io.StringIO()
        sys.stdout = captured
        highest_countries(loaded, rates_from_year(loaded, i + 2003), 3)
        sys.stdout = sys.__stdout__
        pepa = captured.getvalue()
        k = highest[i]
        assert captured.getvalue() == highest[i]


def test_main():
    test_rates_from_year()
    test_lowest_countries()
    test_highest_countries()
    print("All tests passed.")


if __name__ == '__main__':
    test_main()
