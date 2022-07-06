from seleniumbase import BaseCase
import pytest
import time

class TC001_Pomis2A_Report(BaseCase):
    def test_Kichok_Branch_00633(self):
        url="https://timf.imikrof.com/"
        username = "#email"
        password="#password"
        btnLogin="input[value='Login']"
        report_level="#report_level"
        branch="#filter_bazr_info"
        month="select[name='cbo_month']"
        show="(//button[normalize-space()='Show'])[1]"


        self.open_url(url)
        self.type(username, "arman")
        self.type(password, "123456789")
        self.click(btnLogin)

        # PKSF POMIS-2A REPORT
        self.open_url("https://timf.imikrof.com/PKSF_POMIS_2A_REPORT")
        self.type(report_level, "Branch")
        self.type(branch, "0063 - Kichok Branch")
        self.type(month, "March")
        self.click(show)

        #self.wait_for_element_visible('//*[@id="eport_container"]/div/table/tbody/tr[18]/th[6]')
        self.wait(15)
        self.assert_text("POMIS-2A Report (with Service Charge)", "h2 div[align='center']")
        print("Report Open Successfully")

        # Current Month Recovered Total  4+5+6 = 7

        value4 = self.get_text('//*[@id="eport_container"]/div/table/tbody/tr[18]/th[4]')
        regular = float(value4.replace(',', ''))
        print("Regular Amount:", regular)

        value5 = self.get_text('//*[@id="eport_container"]/div/table/tbody/tr[18]/th[5]')
        due = (float(value5.replace(',', '')))
        print("Due Amount:", due)

        value6 = self.get_text('//*[@id="eport_container"]/div/table/tbody/tr[18]/th[6]')
        advance = float(value6.replace(',', ''))
        print("Advance Amount:", advance)

        exp_recovered_total_amount = regular+due+advance
        print("Expected Total Amount:", exp_recovered_total_amount)

        value7 = self.get_text('//*[@id="eport_container"]/div/table/tbody/tr[18]/th[7]')
        act_recovered_total_amount = float(value7.replace(',', ''))
        print("Actual Total Amount:", act_recovered_total_amount)

        self.assert_equal(exp_recovered_total_amount, act_recovered_total_amount)

        if exp_recovered_total_amount == act_recovered_total_amount:
            print("Current Month Recovered Total Match")
        else:
            print("Current Month Recovered Total Don't Match")

        # New Due Amount ( Current Month)  3-4 = 8

        value3= self.get_text('//*[@id="eport_container"]/div/table/tbody/tr[18]/th[3]')
        regLoan_recoverable = float(value3.replace(',', ''))
        print("Loan Recoverable Amount:", regLoan_recoverable)

        value4 = self.get_text('//*[@id="eport_container"]/div/table/tbody/tr[18]/th[4]')
        ramount = float(value4.replace(',', ''))
        print("Regular Amount:", ramount)

        exp_due_amount = regLoan_recoverable-ramount
        print("Expected Due Amount:", exp_due_amount)

        value8 = self.get_text('//*[@id="eport_container"]/div/table/tbody/tr[18]/th[8]')
        act_new_due_amount = float(value8.replace(',', ''))
        print("Actual Due Amount:", act_new_due_amount)

        self.assert_equal(exp_due_amount, act_new_due_amount)

        if exp_due_amount==act_new_due_amount:
            print("New Due Amount Match")
        else:
            print("New Due Amount Don't Match")

        # End of the Month  ( Total Due ) (2-5+8) = 9

        value2 = self.get_text('//*[@id="eport_container"]/div/table/tbody/tr[18]/th[2]')
        due_last_month = float(value2.replace(',', ''))
        print("Due at the end of the Last Month:", due_last_month)

        value5 = self.get_text('//*[@id="eport_container"]/div/table/tbody/tr[18]/th[5]')
        due_amount = float(value5.replace(',', ''))
        print("Due Amount:", due_amount)

        value_8 = self.get_text('//*[@id="eport_container"]/div/table/tbody/tr[18]/th[8]')
        new_due_amount = float(value_8.replace(',', ''))
        print("New Due Amount:", new_due_amount)

        exp_total_due = due_last_month-due_amount+new_due_amount
        print("Expected Total Due:", exp_total_due)

        value9 = self.get_text('//*[@id="eport_container"]/div/table/tbody/tr[18]/th[9]')
        act_end_total_due = float(value9.replace(',', ''))
        print("End of the month total due:", act_end_total_due)

        self.assert_equal(exp_due_amount, act_new_due_amount)

        if exp_due_amount==act_new_due_amount:
            print("End of the month total due match")
        else:
            print("End of the month total due don't match")

    def test_Pirgacha_Branch_0062(self):
        url = "https://timf.imikrof.com/"
        username = "#email"
        password = "#password"
        btnLogin = "input[value='Login']"
        report_level = "#report_level"
        branch = "#filter_bazr_info"
        month = "select[name='cbo_month']"
        show = "(//button[normalize-space()='Show'])[1]"

        self.open_url(url)
        self.type(username, "arman")
        self.type(password, "123456789")
        self.click(btnLogin)

        # PKSF POMIS-2A REPORT
        self.open_url("https://timf.imikrof.com/PKSF_POMIS_2A_REPORT")
        self.type(report_level, "Branch")
        self.type(branch, "0062 - Pirgacha Branch")
        self.type(month, "March")
        self.click(show)

        #self.wait_for_element_visible('//*[@id="eport_container"]/div/table/tbody/tr[18]/th[6]')
        self.wait(15)
        self.assert_text("POMIS-2A Report (with Service Charge)", "h2 div[align='center']")
        print("Report Open Successfully")

        # Current Month Recovered Total  4+5+6 = 7

        value4 = self.get_text('//*[@id="eport_container"]/div/table/tbody/tr[18]/th[4]')
        regular = float(value4.replace(',', ''))
        print("Regular Amount:", regular)

        value5 = self.get_text('//*[@id="eport_container"]/div/table/tbody/tr[18]/th[5]')
        due = (float(value5.replace(',', '')))
        print("Due Amount:", due)

        value6 = self.get_text('//*[@id="eport_container"]/div/table/tbody/tr[18]/th[6]')
        advance = float(value6.replace(',', ''))
        print("Advance Amount:", advance)

        exp_recovered_total_amount = regular + due + advance
        print("Expected Total Amount:", exp_recovered_total_amount)

        value7 = self.get_text('//*[@id="eport_container"]/div/table/tbody/tr[18]/th[7]')
        act_recovered_total_amount = float(value7.replace(',', ''))
        print("Actual Total Amount:", act_recovered_total_amount)

        self.assert_equal(exp_recovered_total_amount, act_recovered_total_amount)

        if exp_recovered_total_amount == act_recovered_total_amount:
            print("Current Month Recovered Total Match")
        else:
            print("Current Month Recovered Total Don't Match")

        # New Due Amount ( Current Month)  3-4 = 8

        value3 = self.get_text('//*[@id="eport_container"]/div/table/tbody/tr[18]/th[3]')
        regLoan_recoverable = float(value3.replace(',', ''))
        print("Loan Recoverable Amount:", regLoan_recoverable)

        value4 = self.get_text('//*[@id="eport_container"]/div/table/tbody/tr[18]/th[4]')
        ramount = float(value4.replace(',', ''))
        print("Regular Amount:", ramount)

        exp_due_amount = regLoan_recoverable - ramount
        print("Expected Due Amount:", exp_due_amount)

        value8 = self.get_text('//*[@id="eport_container"]/div/table/tbody/tr[18]/th[8]')
        act_new_due_amount = float(value8.replace(',', ''))
        print("Actual Due Amount:", act_new_due_amount)

        self.assert_equal(exp_due_amount, act_new_due_amount)

        if exp_due_amount == act_new_due_amount:
            print("New Due Amount Match")
        else:
            print("New Due Amount Don't Match")

        # End of the Month  ( Total Due ) (2-5+8) = 9

        value2 = self.get_text('//*[@id="eport_container"]/div/table/tbody/tr[18]/th[2]')
        due_last_month = float(value2.replace(',', ''))
        print("Due at the end of the Last Month:", due_last_month)

        value5 = self.get_text('//*[@id="eport_container"]/div/table/tbody/tr[18]/th[5]')
        due_amount = float(value5.replace(',', ''))
        print("Due Amount:", due_amount)

        value_8 = self.get_text('//*[@id="eport_container"]/div/table/tbody/tr[18]/th[8]')
        new_due_amount = float(value_8.replace(',', ''))
        print("New Due Amount:", new_due_amount)

        exp_total_due = due_last_month - due_amount + new_due_amount
        print("Expected Total Due:", exp_total_due)

        value9 = self.get_text('//*[@id="eport_container"]/div/table/tbody/tr[18]/th[9]')
        act_end_total_due = float(value9.replace(',', ''))
        print("End of the month total due:", act_end_total_due)

        self.assert_equal(exp_due_amount, act_new_due_amount)

        if exp_due_amount == act_new_due_amount:
            print("End of the month total due match")
        else:
            print("End of the month total due don't match")

    def test_Khorkhori_Branch_0061(self):

        url = "https://timf.imikrof.com/"
        username = "#email"
        password = "#password"
        btnLogin = "input[value='Login']"
        report_level = "#report_level"
        branch = "#filter_bazr_info"
        month = "select[name='cbo_month']"
        show = "(//button[normalize-space()='Show'])[1]"

        self.open_url(url)
        self.type(username, "arman")
        self.type(password, "123456789")
        self.click(btnLogin)

        # PKSF POMIS-2A REPORT
        self.open_url("https://timf.imikrof.com/PKSF_POMIS_2A_REPORT")
        self.type(report_level, "Branch")
        self.type(branch, "0061 - Khorkhori Branch")
        self.type(month, "March")
        self.click(show)

        #self.wait_for_element_visible('//*[@id="eport_container"]/div/table/tbody/tr[18]/th[6]')
        self.wait(15)
        self.assert_text("POMIS-2A Report (with Service Charge)", "h2 div[align='center']")
        print("Report Open Successfully")

        # Current Month Recovered Total  4+5+6 = 7

        value4 = self.get_text('//*[@id="eport_container"]/div/table/tbody/tr[18]/th[4]')
        regular = float(value4.replace(',', ''))
        print("Regular Amount:", regular)

        value5 = self.get_text('//*[@id="eport_container"]/div/table/tbody/tr[18]/th[5]')
        due = (float(value5.replace(',', '')))
        print("Due Amount:", due)

        value6 = self.get_text('//*[@id="eport_container"]/div/table/tbody/tr[18]/th[6]')
        advance = float(value6.replace(',', ''))
        print("Advance Amount:", advance)

        exp_recovered_total_amount = regular + due + advance
        print("Expected Total Amount:", exp_recovered_total_amount)

        value7 = self.get_text('//*[@id="eport_container"]/div/table/tbody/tr[18]/th[7]')
        act_recovered_total_amount = float(value7.replace(',', ''))
        print("Actual Total Amount:", act_recovered_total_amount)

        self.assert_equal(exp_recovered_total_amount, act_recovered_total_amount)

        if exp_recovered_total_amount == act_recovered_total_amount:
            print("Current Month Recovered Total Match")
        else:
            print("Current Month Recovered Total Don't Match")

        # New Due Amount ( Current Month)  3-4 = 8

        value3 = self.get_text('//*[@id="eport_container"]/div/table/tbody/tr[18]/th[3]')
        regLoan_recoverable = float(value3.replace(',', ''))
        print("Loan Recoverable Amount:", regLoan_recoverable)

        value4 = self.get_text('//*[@id="eport_container"]/div/table/tbody/tr[18]/th[4]')
        ramount = float(value4.replace(',', ''))
        print("Regular Amount:", ramount)

        exp_due_amount = regLoan_recoverable - ramount
        print("Expected Due Amount:", exp_due_amount)

        value8 = self.get_text('//*[@id="eport_container"]/div/table/tbody/tr[18]/th[8]')
        act_new_due_amount = float(value8.replace(',', ''))
        print("Actual Due Amount:", act_new_due_amount)

        self.assert_equal(exp_due_amount, act_new_due_amount)

        if exp_due_amount == act_new_due_amount:
            print("New Due Amount Match")
        else:
            print("New Due Amount Don't Match")

        # End of the Month  ( Total Due ) (2-5+8) = 9

        value2 = self.get_text('//*[@id="eport_container"]/div/table/tbody/tr[18]/th[2]')
        due_last_month = float(value2.replace(',', ''))
        print("Due at the end of the Last Month:", due_last_month)

        value5 = self.get_text('//*[@id="eport_container"]/div/table/tbody/tr[18]/th[5]')
        due_amount = float(value5.replace(',', ''))
        print("Due Amount:", due_amount)

        value_8 = self.get_text('//*[@id="eport_container"]/div/table/tbody/tr[18]/th[8]')
        new_due_amount = float(value_8.replace(',', ''))
        print("New Due Amount:", new_due_amount)

        exp_total_due = due_last_month - due_amount + new_due_amount
        print("Expected Total Due:", exp_total_due)

        value9 = self.get_text('//*[@id="eport_container"]/div/table/tbody/tr[18]/th[9]')
        act_end_total_due = float(value9.replace(',', ''))
        print("End of the month total due:", act_end_total_due)

        self.assert_equal(exp_due_amount, act_new_due_amount)

        if exp_due_amount == act_new_due_amount:
            print("End of the month total due match")
        else:
            print("End of the month total due don't match")

    def test_Paba_Branch_0060(self):

        url = "https://timf.imikrof.com/"
        username = "#email"
        password = "#password"
        btnLogin = "input[value='Login']"
        report_level = "#report_level"
        branch = "#filter_bazr_info"
        month = "select[name='cbo_month']"
        show = "(//button[normalize-space()='Show'])[1]"

        self.open_url(url)
        self.type(username, "arman")
        self.type(password, "123456789")
        self.click(btnLogin)

        # PKSF POMIS-2A REPORT
        self.open_url("https://timf.imikrof.com/PKSF_POMIS_2A_REPORT")
        self.type(report_level, "Branch")
        self.type(branch, "0060 - Paba Branch")
        self.type(month, "March")
        self.click(show)

        #self.wait_for_element_visible('//*[@id="eport_container"]/div/table/tbody/tr[18]/th[6]')
        self.wait(20)
        self.assert_text("POMIS-2A Report (with Service Charge)", "h2 div[align='center']")
        print("Report Open Successfully")

        # Current Month Recovered Total     4+5+6 = 7

        value4 = self.get_text('//*[@id="eport_container"]/div/table/tbody/tr[18]/th[4]')
        regular = float(value4.replace(',', ''))
        print("Regular Amount:", regular)

        value5 = self.get_text('//*[@id="eport_container"]/div/table/tbody/tr[18]/th[5]')
        due = (float(value5.replace(',', '')))
        print("Due Amount:", due)

        value6 = self.get_text('//*[@id="eport_container"]/div/table/tbody/tr[18]/th[6]')
        advance = float(value6.replace(',', ''))
        print("Advance Amount:", advance)

        exp_recovered_total_amount = regular + due + advance
        print("Expected Total Amount:", exp_recovered_total_amount)

        value7 = self.get_text('//*[@id="eport_container"]/div/table/tbody/tr[18]/th[7]')
        act_recovered_total_amount = float(value7.replace(',', ''))
        print("Actual Total Amount:", act_recovered_total_amount)

        self.assert_equal(exp_recovered_total_amount, act_recovered_total_amount)

        if exp_recovered_total_amount == act_recovered_total_amount:
            print("Current Month Recovered Total Match")
        else:
            print("Current Month Recovered Total Don't Match")

        # New Due Amount ( Current Month)   3-4 = 8

        value3 = self.get_text('//*[@id="eport_container"]/div/table/tbody/tr[18]/th[3]')
        regLoan_recoverable = float(value3.replace(',', ''))
        print("Loan Recoverable Amount:", regLoan_recoverable)

        value4 = self.get_text('//*[@id="eport_container"]/div/table/tbody/tr[18]/th[4]')
        ramount = float(value4.replace(',', ''))
        print("Regular Amount:", ramount)

        exp_due_amount = regLoan_recoverable - ramount
        print("Expected Due Amount:", exp_due_amount)

        value8 = self.get_text('//*[@id="eport_container"]/div/table/tbody/tr[18]/th[8]')
        act_new_due_amount = float(value8.replace(',', ''))
        print("Actual Due Amount:", act_new_due_amount)

        self.assert_equal(exp_due_amount, act_new_due_amount)

        if exp_due_amount == act_new_due_amount:
            print("New Due Amount Match")
        else:
            print("New Due Amount Don't Match")

        # End of the Month  ( Total Due )   (2-5+8) = 9

        value2 = self.get_text('//*[@id="eport_container"]/div/table/tbody/tr[18]/th[2]')
        due_last_month = float(value2.replace(',', ''))
        print("Due at the end of the Last Month:", due_last_month)

        value5 = self.get_text('//*[@id="eport_container"]/div/table/tbody/tr[18]/th[5]')
        due_amount = float(value5.replace(',', ''))
        print("Due Amount:", due_amount)

        value_8 = self.get_text('//*[@id="eport_container"]/div/table/tbody/tr[18]/th[8]')
        new_due_amount = float(value_8.replace(',', ''))
        print("New Due Amount:", new_due_amount)

        exp_total_due = due_last_month - due_amount + new_due_amount
        print("Expected Total Due:", exp_total_due)

        value9 = self.get_text('//*[@id="eport_container"]/div/table/tbody/tr[18]/th[9]')
        act_end_total_due = float(value9.replace(',', ''))
        print("End of the month total due:", act_end_total_due)

        self.assert_equal(exp_due_amount, act_new_due_amount)

        if exp_due_amount == act_new_due_amount:
            print("End of the month total due match")
        else:
            print("End of the month total due don't match")

    def test_Bornali_Branch_0059(self):

        url = "https://timf.imikrof.com/"
        username = "#email"
        password = "#password"
        btnLogin = "input[value='Login']"
        report_level = "#report_level"
        branch = "#filter_bazr_info"
        month = "select[name='cbo_month']"
        show = "(//button[normalize-space()='Show'])[1]"

        self.open_url(url)
        self.type(username, "arman")
        self.type(password, "123456789")
        self.click(btnLogin)

        # PKSF POMIS-2A REPORT
        self.open_url("https://timf.imikrof.com/PKSF_POMIS_2A_REPORT")
        self.type(report_level, "Branch")
        self.type(branch, "0059 - Bornali Branch")
        self.type(month, "March")
        self.click(show)

        # self.wait_for_element_visible('//*[@id="eport_container"]/div/table/tbody/tr[18]/th[6]')
        self.wait(15)
        self.assert_text("POMIS-2A Report (with Service Charge)", "h2 div[align='center']")
        print("Report Open Successfully")

        # Current Month Recovered Total     4+5+6 = 7

        value4 = self.get_text('//*[@id="eport_container"]/div/table/tbody/tr[18]/th[4]')
        regular = float(value4.replace(',', ''))
        print("Regular Amount:", regular)

        value5 = self.get_text('//*[@id="eport_container"]/div/table/tbody/tr[18]/th[5]')
        due = (float(value5.replace(',', '')))
        print("Due Amount:", due)

        value6 = self.get_text('//*[@id="eport_container"]/div/table/tbody/tr[18]/th[6]')
        advance = float(value6.replace(',', ''))
        print("Advance Amount:", advance)

        exp_recovered_total_amount = regular + due + advance
        print("Expected Total Amount:", exp_recovered_total_amount)

        value7 = self.get_text('//*[@id="eport_container"]/div/table/tbody/tr[18]/th[7]')
        act_recovered_total_amount = float(value7.replace(',', ''))
        print("Actual Total Amount:", act_recovered_total_amount)

        self.assert_equal(exp_recovered_total_amount, act_recovered_total_amount)

        if exp_recovered_total_amount == act_recovered_total_amount:
            print("Current Month Recovered Total Match")
        else:
            print("Current Month Recovered Total Don't Match")

        # New Due Amount ( Current Month)   3-4 = 8

        value3 = self.get_text('//*[@id="eport_container"]/div/table/tbody/tr[18]/th[3]')
        regLoan_recoverable = float(value3.replace(',', ''))
        print("Loan Recoverable Amount:", regLoan_recoverable)

        value4 = self.get_text('//*[@id="eport_container"]/div/table/tbody/tr[18]/th[4]')
        ramount = float(value4.replace(',', ''))
        print("Regular Amount:", ramount)

        exp_due_amount = regLoan_recoverable - ramount
        print("Expected Due Amount:", exp_due_amount)

        value8 = self.get_text('//*[@id="eport_container"]/div/table/tbody/tr[18]/th[8]')
        act_new_due_amount = float(value8.replace(',', ''))
        print("Actual Due Amount:", act_new_due_amount)

        self.assert_equal(exp_due_amount, act_new_due_amount)

        if exp_due_amount == act_new_due_amount:
            print("New Due Amount Match")
        else:
            print("New Due Amount Don't Match")

        # End of the Month  ( Total Due )   (2-5+8) = 9

        value2 = self.get_text('//*[@id="eport_container"]/div/table/tbody/tr[18]/th[2]')
        due_last_month = float(value2.replace(',', ''))
        print("Due at the end of the Last Month:", due_last_month)

        value5 = self.get_text('//*[@id="eport_container"]/div/table/tbody/tr[18]/th[5]')
        due_amount = float(value5.replace(',', ''))
        print("Due Amount:", due_amount)

        value_8 = self.get_text('//*[@id="eport_container"]/div/table/tbody/tr[18]/th[8]')
        new_due_amount = float(value_8.replace(',', ''))
        print("New Due Amount:", new_due_amount)

        exp_total_due = due_last_month - due_amount + new_due_amount
        print("Expected Total Due:", exp_total_due)

        value9 = self.get_text('//*[@id="eport_container"]/div/table/tbody/tr[18]/th[9]')
        act_end_total_due = float(value9.replace(',', ''))
        print("End of the month total due:", act_end_total_due)

        self.assert_equal(exp_due_amount, act_new_due_amount)

        if exp_due_amount == act_new_due_amount:
            print("End of the month total due match")
        else:
            print("End of the month total due don't match")

    def test_Baludanga_Branch_0058(self):

        url = "https://timf.imikrof.com/"
        username = "#email"
        password = "#password"
        btnLogin = "input[value='Login']"
        report_level = "#report_level"
        branch = "#filter_bazr_info"
        month = "select[name='cbo_month']"
        show = "(//button[normalize-space()='Show'])[1]"

        self.open_url(url)
        self.type(username, "arman")
        self.type(password, "123456789")
        self.click(btnLogin)

        # PKSF POMIS-2A REPORT
        self.open_url("https://timf.imikrof.com/PKSF_POMIS_2A_REPORT")
        self.type(report_level, "Branch")
        self.type(branch, "0058 - Baludanga Branch")
        self.type(month, "March")
        self.click(show)

        # self.wait_for_element_visible('//*[@id="eport_container"]/div/table/tbody/tr[18]/th[6]')
        self.wait(15)
        self.assert_text("POMIS-2A Report (with Service Charge)", "h2 div[align='center']")
        print("Report Open Successfully")

        # Current Month Recovered Total     4+5+6 = 7

        value4 = self.get_text('//*[@id="eport_container"]/div/table/tbody/tr[18]/th[4]')
        regular = float(value4.replace(',', ''))
        print("Regular Amount:", regular)

        value5 = self.get_text('//*[@id="eport_container"]/div/table/tbody/tr[18]/th[5]')
        due = (float(value5.replace(',', '')))
        print("Due Amount:", due)

        value6 = self.get_text('//*[@id="eport_container"]/div/table/tbody/tr[18]/th[6]')
        advance = float(value6.replace(',', ''))
        print("Advance Amount:", advance)

        exp_recovered_total_amount = regular + due + advance
        print("Expected Total Amount:", exp_recovered_total_amount)

        value7 = self.get_text('//*[@id="eport_container"]/div/table/tbody/tr[18]/th[7]')
        act_recovered_total_amount = float(value7.replace(',', ''))
        print("Actual Total Amount:", act_recovered_total_amount)

        self.assert_equal(exp_recovered_total_amount, act_recovered_total_amount)

        if exp_recovered_total_amount == act_recovered_total_amount:
            print("Current Month Recovered Total Match")
        else:
            print("Current Month Recovered Total Don't Match")

        # New Due Amount ( Current Month)   3-4 = 8

        value3 = self.get_text('//*[@id="eport_container"]/div/table/tbody/tr[18]/th[3]')
        regLoan_recoverable = float(value3.replace(',', ''))
        print("Loan Recoverable Amount:", regLoan_recoverable)

        value4 = self.get_text('//*[@id="eport_container"]/div/table/tbody/tr[18]/th[4]')
        ramount = float(value4.replace(',', ''))
        print("Regular Amount:", ramount)

        exp_due_amount = regLoan_recoverable - ramount
        print("Expected Due Amount:", exp_due_amount)

        value8 = self.get_text('//*[@id="eport_container"]/div/table/tbody/tr[18]/th[8]')
        act_new_due_amount = float(value8.replace(',', ''))
        print("Actual Due Amount:", act_new_due_amount)

        self.assert_equal(exp_due_amount, act_new_due_amount)

        if exp_due_amount == act_new_due_amount:
            print("New Due Amount Match")
        else:
            print("New Due Amount Don't Match")


        # End of the Month  ( Total Due )       (2-5+8) = 9

        value2 = self.get_text('//*[@id="eport_container"]/div/table/tbody/tr[18]/th[2]')
        due_last_month = float(value2.replace(',', ''))
        print("Due at the end of the Last Month:", due_last_month)

        value5 = self.get_text('//*[@id="eport_container"]/div/table/tbody/tr[18]/th[5]')
        due_amount = float(value5.replace(',', ''))
        print("Due Amount:", due_amount)

        value_8 = self.get_text('//*[@id="eport_container"]/div/table/tbody/tr[18]/th[8]')
        new_due_amount = float(value_8.replace(',', ''))
        print("New Due Amount:", new_due_amount)

        exp_total_due = due_last_month - due_amount + new_due_amount
        print("Expected Total Due:", exp_total_due)

        value9 = self.get_text('//*[@id="eport_container"]/div/table/tbody/tr[18]/th[9]')
        act_end_total_due = float(value9.replace(',', ''))
        print("End of the month total due:", act_end_total_due)

        self.assert_equal(exp_due_amount, act_new_due_amount)

        if exp_due_amount == act_new_due_amount:
            print("End of the month total due match")
        else:
            print("End of the month total due don't match")