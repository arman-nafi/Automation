from seleniumbase import BaseCase
import pytest
import time


set_report_level = "Branch"
set_month = "March"
set_year = "2022"
set_loan_option = "Loan Product"

class TC001_Pomis1_Report(BaseCase):
    def test_Kichok_Branch_0063(self):

        url="https://timf.imikrof.com/"
        username = "#email"
        password="#password"
        btnLogin="input[value='Login']"

        report_level="#report_level"
        #branch="#filter_bazr_info"
        month="select[name='cbo_month']"
        year = "select[name='cbo_year']"
        loan_option = "select[name='loan_option']"
        show="//button[normalize-space()='Show']"


        self.open_url(url)
        self.type(username, "arman")
        self.type(password, "123456789")
        self.click(btnLogin)
        print("Login Successful")

        # Pomis-1 Reports
        self.open_url("https://timf.imikrof.com/PKSF_POMIS_1_REPORT")
        self.type(report_level, set_report_level)
        #self.type(branch, "0063 - Kichok Branch")
        self.type(month, set_month)
        self.type(year, set_year)
        self.type(loan_option, set_loan_option)
        self.click(show)

        #self.wait_for_element_visible('//*[@id="DivIdToPrint"]/div/table[2]/tbody/tr[10]/td[5]')
        self.wait(10)

        self.assert_text("POMIS-1 Report", "h2 div[align='center']")
        print("Report Open Successfully")

        # Statement of Samity and Member

        # NO OF SAMITY (3+4=5)

        samity_male3 = self.get_text('//*[@id="DivIdToPrint"]/div/table[2]/tbody/tr[6]/td[3]')
        print("Samity Male:", samity_male3)

        samity_female4 = self.get_text('//*[@id="DivIdToPrint"]/div/table[2]/tbody/tr[6]/td[4]')
        print("Samity Female:", samity_female4)

        exp_samity_total = str(int(samity_male3) + int(samity_female4))
        print("Expected Total:", exp_samity_total)

        act_samity_total = self.get_text('//*[@id="DivIdToPrint"]/div/table[2]/tbody/tr[6]/td[5]')
        print("Actual Total:", act_samity_total)



        if exp_samity_total==act_samity_total:
            print("No of Samity Match")
        else:
            print("No of Samity Don't Match")


        # NO OF MEMBER (6+7=8)

        member_male6 = self.get_text('//*[@id="DivIdToPrint"]/div/table[2]/tbody/tr[6]/td[6]')
        print("Member Male:", member_male6)

        member_female7 = self.get_text('//*[@id="DivIdToPrint"]/div/table[2]/tbody/tr[6]/td[7]')
        print("Member Female:", member_female7)

        exp_member_total = str(int(member_male6)+int(member_female7))
        print("Expected Total:", exp_member_total)

        act_member_total = self.get_text('//*[@id="DivIdToPrint"]/div/table[2]/tbody/tr[6]/td[8]')
        print("Actual Member Total:", act_member_total)

        self.assert_equal(exp_member_total, act_member_total)

        if exp_member_total==act_member_total:
            print("No of Member Match")
        else:
            print("No of Member Don't Match")


        # Statement Of Savings (8+9=10)

        value8 = self.get_text('//*[@id="DivIdToPrint"]/div/table[3]/tbody/tr[22]/td[5]')
        clb_male = float(value8.replace(',', ''))
        print("Closing Balance Male:", clb_male)

        value9 = self.get_text('//*[@id="DivIdToPrint"]/div/table[3]/tbody/tr[22]/td[6]')
        clb_female = float(value9.replace(',', ''))
        print("Closing Balance Female:", clb_female)

        exp_clb_total = clb_male+clb_female
        print("Expected Closing Balance:", exp_clb_total)

        value10 = self.get_text('//*[@id="DivIdToPrint"]/div/table[3]/tbody/tr[22]/td[7]')
        act_clb_total = float(value10.replace(',', ''))
        print("Actual Closing Balance:", act_clb_total)

        self.assert_equal(exp_clb_total, act_clb_total)

        if exp_clb_total==act_clb_total:
            print("Closing Balance Match")
        else:
            print("Closing Balance Don't Match")

        self.assert_equal(exp_samity_total, act_samity_total)

    def test_Pirgacha_Branch_0062(self):

        url = "https://timf.imikrof.com/"
        username = "#email"
        password = "#password"
        btnLogin = "input[value='Login']"
        report_level = "#report_level"
        branch = "#filter_bazr_info"
        month = "select[name='cbo_month']"
        show = "//button[normalize-space()='Show']"

        self.open_url(url)
        self.type(username, "arman")
        self.type(password, "123456789")
        self.click(btnLogin)
        print("Login Successful")

        # Central Branch
        self.open_url("https://timf.imikrof.com/PKSF_POMIS_1_REPORT")
        self.type(report_level, "Branch")
        self.type(branch, "0062 - Pirgacha Branch")
        self.type(month, "March")
        self.click(show)

        # self.wait_for_element_visible('//*[@id="DivIdToPrint"]/div/table[2]/tbody/tr[10]/td[5]')
        self.wait(10)

        self.assert_text("POMIS-1 Report", "h2 div[align='center']")
        print("Report Open Successfully")

        # Statement of Samity and Member

        # NO OF SAMITY (3+4=5)

        samity_male3 = self.get_text('//*[@id="DivIdToPrint"]/div/table[2]/tbody/tr[6]/td[3]')
        print("Samity Male:", samity_male3)

        samity_female4 = self.get_text('//*[@id="DivIdToPrint"]/div/table[2]/tbody/tr[6]/td[4]')
        print("Samity Female:", samity_female4)

        exp_samity_total = str(int(samity_male3) + int(samity_female4))
        print("Expected Total:", exp_samity_total)

        act_samity_total = self.get_text('//*[@id="DivIdToPrint"]/div/table[2]/tbody/tr[6]/td[5]')
        print("Actual Total:", act_samity_total)

        if exp_samity_total == act_samity_total:
            print("No of Samity Match")
        else:
            print("No of Samity Don't Match")

        # NO OF MEMBER (6+7=8)

        member_male6 = self.get_text('//*[@id="DivIdToPrint"]/div/table[2]/tbody/tr[6]/td[6]')
        print("Member Male:", member_male6)

        member_female7 = self.get_text('//*[@id="DivIdToPrint"]/div/table[2]/tbody/tr[6]/td[7]')
        print("Member Female:", member_female7)

        exp_member_total = str(int(member_male6) + int(member_female7))
        print("Expected Total:", exp_member_total)

        act_member_total = self.get_text('//*[@id="DivIdToPrint"]/div/table[2]/tbody/tr[6]/td[8]')
        print("Actual Member Total:", act_member_total)

        self.assert_equal(exp_member_total, act_member_total)

        if exp_member_total == act_member_total:
            print("No of Member Match")
        else:
            print("No of Member Don't Match")

        # Statement Of Savings (8+9=10)

        value8 = self.get_text('//*[@id="DivIdToPrint"]/div/table[3]/tbody/tr[22]/td[5]')
        clb_male = float(value8.replace(',', ''))
        print("Closing Balance Male:", clb_male)

        value9 = self.get_text('//*[@id="DivIdToPrint"]/div/table[3]/tbody/tr[22]/td[6]')
        clb_female = float(value9.replace(',', ''))
        print("Closing Balance Female:", clb_female)

        exp_clb_total = clb_male + clb_female
        print("Expected Closing Balance:", exp_clb_total)

        value10 = self.get_text('//*[@id="DivIdToPrint"]/div/table[3]/tbody/tr[22]/td[7]')
        act_clb_total = float(value10.replace(',', ''))
        print("Actual Closing Balance:", act_clb_total)

        self.assert_equal(exp_clb_total, act_clb_total)

        if exp_clb_total == act_clb_total:
            print("Closing Balance Match")
        else:
            print("Closing Balance Don't Match")

        self.assert_equal(exp_samity_total, act_samity_total)

    def test_Khorkhori_Branch_0061(self):

        url = "https://timf.imikrof.com/"
        username = "#email"
        password = "#password"
        btnLogin = "input[value='Login']"
        report_level = "#report_level"
        branch = "#filter_bazr_info"
        month = "select[name='cbo_month']"
        show = "//button[normalize-space()='Show']"

        self.open_url(url)
        self.type(username, "arman")
        self.type(password, "123456789")
        self.click(btnLogin)
        print("Login Successful")

        # Central Branch
        self.open_url("https://timf.imikrof.com/PKSF_POMIS_1_REPORT")
        self.type(report_level, "Branch")
        self.type(branch, "0061 - Khorkhori Branch")
        self.type(month, "March")
        self.click(show)

        # self.wait_for_element_visible('//*[@id="DivIdToPrint"]/div/table[2]/tbody/tr[10]/td[5]')
        self.wait(10)

        self.assert_text("POMIS-1 Report", "h2 div[align='center']")
        print("Report Open Successfully")

        # Statement of Samity and Member

        # NO OF SAMITY (3+4=5)

        samity_male3 = self.get_text('//*[@id="DivIdToPrint"]/div/table[2]/tbody/tr[6]/td[3]')
        print("Samity Male:", samity_male3)

        samity_female4 = self.get_text('//*[@id="DivIdToPrint"]/div/table[2]/tbody/tr[6]/td[4]')
        print("Samity Female:", samity_female4)

        exp_samity_total = str(int(samity_male3) + int(samity_female4))
        print("Expected Total:", exp_samity_total)

        act_samity_total = self.get_text('//*[@id="DivIdToPrint"]/div/table[2]/tbody/tr[6]/td[5]')
        print("Actual Total:", act_samity_total)

        if exp_samity_total == act_samity_total:
            print("No of Samity Match")
        else:
            print("No of Samity Don't Match")


        # NO OF MEMBER (6+7=8)

        member_male6 = self.get_text('//*[@id="DivIdToPrint"]/div/table[2]/tbody/tr[6]/td[6]')
        print("Member Male:", member_male6)

        member_female7 = self.get_text('//*[@id="DivIdToPrint"]/div/table[2]/tbody/tr[6]/td[7]')
        print("Member Female:", member_female7)

        exp_member_total = str(int(member_male6) + int(member_female7))
        print("Expected Total:", exp_member_total)

        act_member_total = self.get_text('//*[@id="DivIdToPrint"]/div/table[2]/tbody/tr[6]/td[8]')
        print("Actual Member Total:", act_member_total)

        self.assert_equal(exp_member_total, act_member_total)

        if exp_member_total == act_member_total:
            print("No of Member Match")
        else:
            print("No of Member Don't Match")

        # Statement Of Savings (8+9=10)

        value8 = self.get_text('//*[@id="DivIdToPrint"]/div/table[3]/tbody/tr[22]/td[5]')
        clb_male = float(value8.replace(',', ''))
        print("Closing Balance Male:", clb_male)

        value9 = self.get_text('//*[@id="DivIdToPrint"]/div/table[3]/tbody/tr[22]/td[6]')
        clb_female = float(value9.replace(',', ''))
        print("Closing Balance Female:", clb_female)

        exp_clb_total = clb_male + clb_female
        print("Expected Closing Balance:", exp_clb_total)

        value10 = self.get_text('//*[@id="DivIdToPrint"]/div/table[3]/tbody/tr[22]/td[7]')
        act_clb_total = float(value10.replace(',', ''))
        print("Actual Closing Balance:", act_clb_total)

        self.assert_equal(exp_clb_total, act_clb_total)

        if exp_clb_total == act_clb_total:
            print("Closing Balance Match")
        else:
            print("Closing Balance Don't Match")

        self.assert_equal(exp_samity_total, act_samity_total)


























