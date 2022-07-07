from seleniumbase import BaseCase
import pytest
import time



set_report_level = "Branch"
set_month = "June"
set_year = "2022"
#set_loan_option = "Loan Product"

class TC001_Pomis1_Report(BaseCase):
    def test_all_branch(self):

        url = "https://timf.imikrof.com/"
        username = "#email"
        password = "#password"
        btnLogin = "input[value='Login']"

        report_level = "#report_level"
        # branch="#filter_bazr_info"
        month = "select[name='cbo_month']"
        year = "select[name='cbo_year']"
        loan_option = "select[name='loan_option']"
        show = "//button[normalize-space()='Show']"

        self.open_url(url)
        self.maximize_window()
        self.type(username, "arman")
        self.type(password, "123456789")
        self.click(btnLogin)
        print("Login Successful")

        self.wait(2)


        # Pomis-1 Reports
        self.open_url("https://timf.imikrof.com/PKSF_POMIS_1_REPORT")
        self.wait(2)
        self.type(report_level, set_report_level)
        self.type(month, set_month)
        self.type(year, set_year)
        #self.type(loan_option, set_loan_option)
        self.click(show)

        # self.wait_for_element_visible('//*[@id="DivIdToPrint"]/div/table[2]/tbody/tr[10]/td[5]')
        self.wait(20)

        self.assert_text("POMIS-1 Report", "h2 div[align='center']")
        print("Report Open Successfully")

        # Statement of Samity and Member

        # NO OF SAMITY (3+4=5)

        samity_male3 = self.get_text('tbody tr:nth-child(13) th:nth-child(3) div:nth-child(1)')
        print("Samity Male:", samity_male3)

        samity_female4 = self.get_text('tbody tr:nth-child(13) th:nth-child(3) div:nth-child(1)')
        print("Samity Female:", samity_female4)

        exp_samity_total = str(int(samity_male3) + int(samity_female4))
        print("Expected Total:", exp_samity_total)

        act_samity_total = self.get_text('tbody tr:nth-child(13) th:nth-child(3) div:nth-child(1)')
        print("Actual Total:", act_samity_total)

        if exp_samity_total == act_samity_total:
            print("No of Samity Match")
        else:
            print("No of Samity Don't Match")

        # NO OF MEMBER (6+7=8)

        member_male6 = self.get_text('//*[@id="DivIdToPrint"]/div/table[3]/tbody/tr[13]/th[6]/div')
        print("Member Male:", member_male6)

        member_female7 = self.get_text('//*[@id="DivIdToPrint"]/div/table[3]/tbody/tr[13]/th[7]/div')
        print("Member Female:", member_female7)

        exp_member_total = str(int(member_male6) + int(member_female7))
        print("Expected Total:", exp_member_total)

        act_member_total = self.get_text('//*[@id="DivIdToPrint"]/div/table[3]/tbody/tr[13]/th[8]/div')
        print("Actual Member Total:", act_member_total)

        self.assert_equal(exp_member_total, act_member_total)

        if exp_member_total == act_member_total:
            print("No of Member Match")
        else:
            print("No of Member Don't Match")

        # Statement Of Savings (8+9=10)

        value8 = self.get_text('//*[@id="DivIdToPrint"]/div/table[4]/tbody/tr[78]/td[4]')
        clb_male = float(value8.replace(',', ''))
        print("Closing Balance Male:", clb_male)

        value9 = self.get_text('//*[@id="DivIdToPrint"]/div/table[4]/tbody/tr[78]/td[5]')
        clb_female = float(value9.replace(',', ''))
        print("Closing Balance Female:", clb_female)

        exp_clb_total = clb_male + clb_female
        print("Expected Closing Balance:", exp_clb_total)

        value10 = self.get_text('//*[@id="DivIdToPrint"]/div/table[4]/tbody/tr[78]/td[6]')
        act_clb_total = float(value10.replace(',', ''))
        print("Actual Closing Balance:", act_clb_total)

        self.assert_equal(exp_clb_total, act_clb_total)

        if exp_clb_total == act_clb_total:
            print("Closing Balance Match")
        else:
            print("Closing Balance Don't Match")

        self.assert_equal(exp_samity_total, act_samity_total)

        value2 = self.get_text('//*[@id="DivIdToPrint"]/div/table[5]/tbody/tr[11]/td[2]/div')
        member_last_month = float(value2.replace(',', ''))
        print("TOTAL MEMBER END OF LAST MONTH:", member_last_month)

        value3 = self.get_text('//*[@id="DivIdToPrint"]/div/table[5]/tbody/tr[11]/td[3]/div')
        new_member_crnt_month = float(value3.replace(',', ''))
        print("NEW MEMBER ADMISSION (CURRENT MONTH):", new_member_crnt_month)

        value4 = self.get_text('//*[@id="DivIdToPrint"]/div/table[5]/tbody/tr[11]/td[4]/div')
        member_cancellation = float(value4.replace(',', ''))
        print("MEMBER CANCELLATION (CURRENT MONTH):", member_cancellation)

        exp_total_member = member_last_month + new_member_crnt_month - member_cancellation
        print("EXPECTED TOTAL MEMBER (END OF CURRENT MONTH):", exp_total_member)

        value5 = self.get_text('//*[@id="DivIdToPrint"]/div/table[5]/tbody/tr[11]/td[5]/div')
        act_total_member = float(value5.replace(',', ''))
        print("ACTUAL TOTAL MEMBER (END OF CURRENT MONTH):", act_total_member)

        if exp_total_member == act_total_member:
            print("TOTAL MEMBER (END OF CURRENT MONTH) MATCH")
        else:
            print("TOTAL MEMBER (END OF CURRENT MONTH) DON'T MATCH")



