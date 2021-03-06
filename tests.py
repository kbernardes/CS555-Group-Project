import unittest
from gedcom_parser import test_us02_birth_b4_marriage, test_us03_birth_b4_death, test_us04_marr_b4_divorce, test_us05_marr_b4_death, test_us06_div_b4_death, test_us07_less_than_150, test_us08_birth_b4_marr_parents, test_us09_birth_b4_death_parents, \
test_us_10_marriage_after_14, test_us_11_no_bigamy, test_us12_parents_not_too_old, test_us13_siblings_spacing, test_us14_multiple_births_lessthan_5, test_us15_fewer_than_15_siblings, test_us16_male_last_names, test_us17_no_marriages_to_children, \
test_us18_siblings_should_not_marry, test_us19_first_cousins_should_not_marry, test_us21_correct_gender_role, test_us22_unique_IDs, test_us23_unique_name_and_birth_date, test_us24_unique_families_by_spouses, test_us25_unique_first_names_in_families, test_us26_corresponding_entries,\
test_us27_include_individual_ages, test_us28_order_siblings_by_age,  test_us29_list_deceased, test_us32_list_multiple_births, test_us33_list_orphans, test_us35_list_recent_births, test_us36_list_recent_deaths, test_us38_list_upcoming_birthdays

class TestUM(unittest.TestCase):
    def setUp(self):
        pass

    def test_us02(self):
        self.assertEqual(test_us02_birth_b4_marriage(), "Error: Family: @F2@: US02: Birth before married 8 SEP 2020")

    def test_03(self):
        self.assertEqual(test_us03_birth_b4_death(), "Error: Indi: @I4@ US03: Death 1 NOV 2001 before Birthday 28 MAR 1800")

    def test_us04(self):
        self.assertEqual(test_us04_marr_b4_divorce(), "Error: Family: @F3@: US04: Divorced 3 FEB 1995 before married 6 AUG 1995")

    def test_us05(self):
        self.assertEqual(test_us05_marr_b4_death(), "Error: Family: @F2@: US05: Death of husband before married 8 SEP 2020")

    def test_us06(self):
        self.assertEqual(test_us06_div_b4_death(), "Error: Family: @F6@: US06: Died before divorce 2 FEB 2020")

    def test_us07(self):
        self.assertEqual(test_us07_less_than_150(), "Error: Individual: @I4@: US07: Over 150 years old")

    def test_us08(self):
        self.assertEqual(test_us08_birth_b4_marr_parents(), "Error: Individual: @I2@: US08: born after marriage of parents")

    def test_us09(self):
        self.assertEqual(test_us09_birth_b4_death_parents(), "Error: Individual: @I10@: US09 born 9 months after death of dad")

    def test_us10(self):
        self.assertEqual(test_us_10_marriage_after_14(), "Error: Family: @F1@: US10: Individuals were married before both were 14")

    def test_us11(self):
        self.assertEqual(test_us_11_no_bigamy(), "Error: Individual: @I10@: US11: Individual is married to multiple people")

    def test_us12(self):
        self.assertEqual(test_us12_parents_not_too_old(), "Error: Family: @F2@: US12: Parents are too old")

    def test_us13(self):
        self.assertEqual(test_us13_siblings_spacing(), "Error: Family: @F3@: US13: Siblings too close in age")

    def test_us14(self):
        self.assertEqual(test_us14_multiple_births_lessthan_5(), "Error: Family: @F3@: US14 has more than 5 children with the same birth")

    def test_us15(self):
        self.assertEqual(test_us15_fewer_than_15_siblings(), "Error: Family: @F3@: US15 has 15 or more children")

    def test_us16(self):
        self.assertEqual(test_us16_male_last_names(), "Error: Family: @F1@: US16 has inconsistant male last name")

    def test_us17(self):
        self.assertEqual(test_us17_no_marriages_to_children(), "Error: Family @F12@: US17: Parent is married to child")

    def test_us18(self):
        self.assertEqual(test_us18_siblings_should_not_marry(), "Error: Indi: @I4@: US18: Siblings can't be married")

    def test_us19(self):
        self.assertEqual(test_us19_first_cousins_should_not_marry(), "Error: Indi: @I1@@I1@: US19: First cousins should not marry")

    def test_us21(self):
        self.assertEqual(test_us21_correct_gender_role(), "Error: Family: @F11@: US21: Wife is wrong gender")

    def test_us22(self):
        self.assertEqual(test_us22_unique_IDs(), "Error: Individual: US22: Duplicate ID number")

    def test_us23(self):
        self.assertEqual(test_us23_unique_name_and_birth_date(), ["Error: Individual: @I28@: US23: Does not have a unique name and birthday", "Error: Individual: @I29@: US23: Does not have a unique name and birthday"])

    def test_us24(self):
        self.assertEqual(test_us24_unique_families_by_spouses(), ["Error: Family: @F8@: US24: Does not have a unique husband, wife, and marriage date","Error: Family: @F9@: US24: Does not have a unique husband, wife, and marriage date","Error: Family: @F10@: US24: Does not have a unique husband, wife, and marriage date","Error: Family: @F12@: US24: Does not have a unique husband, wife, and marriage date"])

    def test_us25(self):
        self.assertEqual(test_us25_unique_first_names_in_families(),['Error: Family: @F3@: US25: Does not have unique sibling names and birthdays', 'Error: Family: @F5@: US25: Does not have unique sibling names and birthdays', 'Error: Family: @F12@: US25: Does not have unique sibling names and birthdays'])

    def test_us26(self):
        self.assertEqual(test_us26_corresponding_entries(),'Error Individual:@I4@ US26 individual table and family table do not match')

    def test_us27(self):
        self.assertEqual(test_us27_include_individual_ages(), "US27: Include individual ages: @I41@ 26")

    def test_us28(self):
        self.assertEqual(test_us28_order_siblings_by_age(), "US28: Order siblings from oldest to youngest: @F12@ [23]")

    def test_us29(self):
        self.assertEqual(test_us29_list_deceased(), "US29: List of all deaths in tree: ['Jay /Rana/', 'Angelina /Iannacone/', 'Jacob Davidson /Davidson/', 'Dev /Rana/', 'Jonathan /Dixon/', 'Angela /Rana/', 'Alex /Johnson/']")

    def test_us32(self):
        self.assertEqual(test_us32_list_multiple_births(), "US32: List of all multiple births: [{'Siblings': ['@I21@: Lisa /Iannacone/', '@I22@: Matt /Iannacone/'], 'Fam ID': '@F3@', 'Birth': '10 FEB 1995'}, {'Siblings': ['@I8@: Angelina /Iannacone/', '@I11@: Monica /Iannacone/', '@I15@: Junior /Iannacone/', '@I16@: Dominic /Iannacone/', '@I17@: John /Iannacone/', '@I18@: Jane /Iannacone/'], 'Fam ID': '@F3@', 'Birth': '10 MAY 1989'}, {'Siblings': ['@I24@: Luke /Iannacone/', '@I27@: Danielle /Iannacone/'], 'Fam ID': '@F3@', 'Birth': '10 AUG 1996'}, {'Siblings': ['@I19@: Joe /Iannacone/', '@I20@: Mary /Iannacone/'], 'Fam ID': '@F3@', 'Birth': '10 MAY 1990'}, {'Siblings': ['@I28@: Jane /Fairfield/', '@I29@: Jane /Fairfield/'], 'Fam ID': '@F5@', 'Birth': '11 APR 2015'}, {'Siblings': ['@I35@: Peter /Iannacone2/', '@I35@: Peter /Iannacone2/', '@I35@: Peter /Iannacone2/'], 'Fam ID': '@F12@', 'Birth': '10 AUG 1996'}]")

    def test_us33(self):
        self.assertEqual(test_us33_list_orphans(), "US33: List of all orphans: ['John /Davidson/', 'Bob /Johnson/']")

    def test_us35(self):
        self.assertEqual(test_us35_list_recent_births(), "US35: List of all individuals born within the last 30 days: ['Maria /Iannacone/']")

    def test_us36(self):
        self.assertEqual(test_us36_list_recent_deaths(), "US36: List of all individuals who died within the last 30 days: ['Jonathan /Dixon/']")

    def test_us38(self):
        self.assertEqual(test_us38_list_upcoming_birthdays(), "US38: List of all individuals whose birthdays are in the next 30 days: ['Monica /Iannacone/', 'Dominic /Iannacone/', 'Junior /Iannacone/', 'Dominic /Iannacone/', 'John /Iannacone/', 'Jane /Iannacone/', 'Joe /Iannacone/', 'Mary /Iannacone/', 'John /Smith/']")



if __name__ == '__main__':
    unittest.main()





# test_us02_birth_b4_marriage()

# test_us03_birth_b4_death()

# test_us04_marr_b4_divorce()

# test_us05_marr_b4_death()
# test_us06_div_b4_death()

# test_us07_less_than_150()

# test_us08_birth_b4_marr_parents()

# test_us09_birth_b4_death_parents()



# gedcom_parser.test_us02_birth_b4_marriage()

# gedcom_parser.test_us03_birth_b4_death()


# gedcom_parser.test_us04_marr_b4_divorce()

# gedcom_parser.test_us05_marr_b4_death()
# gedcom_parser.test_us06_div_b4_death()

# gedcom_parser.test_us07_less_than_150()

# gedcom_parser.test_us08_birth_b4_marr_parents()

# gedcom_parser.test_us09_birth_b4_death_parents()