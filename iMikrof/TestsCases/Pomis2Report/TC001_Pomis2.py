from seleniumbase import BaseCase
import pytest
import time

class TC001_Pomis2_Report(BaseCase):
    def test_Kichok_Branch_0063(self):

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

        # PKSF POMIS-2 REPORT
        self.open_url("https://timf.imikrof.com/REPORT_PKSF_POMIS_2")
        self.type(report_level, "Branch")
        self.type(branch, "0063 - Kichok Branch")
        self.type(month, "March")
        self.click(show)

        self.wait(20)

        self.assert_text("POMIS-2 Report (with Service Charge)", "h2 div[align='center']" )
        print("Report Open Successfully")

        #At the End of the Month  ( Borrower No )  (2+4)-7 = 8

        borrower1 = self.get_text('//*[@id="DivIdToPrint"]/table[2]/tbody/tr[18]/th[2]/div')
        print("Borrower No:", borrower1)

        borrower2 = self.get_text('//*[@id="DivIdToPrint"]/table[2]/tbody/tr[18]/th[4]/div')
        print("Borrower No:", borrower2)

        paid_borrower = self.get_text('//*[@id="DivIdToPrint"]/table[2]/tbody/tr[18]/th[7]')
        print("Paid Borrower:", paid_borrower)

        exp_total_borrower = str(int(borrower1)+int(borrower2)-int(paid_borrower))
        print("Expected Total Borrower:", exp_total_borrower)

        total_borrower = self.get_text('//*[@id="DivIdToPrint"]/table[2]/tbody/tr[18]/th[8]/div')
        print("Actual Total Borrower:", total_borrower)

        self.assert_equal(exp_total_borrower, total_borrower)

        if exp_total_borrower==total_borrower:
            print("Expected and Actual Borrower Match")
        else:
            print("Expected and Actual Borrower Doesn't Match")

        # At the End of the Month  ( Amount )  (3+5)-6 = 9

        value1 = self.get_text('//*[@id="DivIdToPrint"]/table[2]/tbody/tr[18]/th[3]/div')
        loan_outstanding = float(value1.replace(',', ''))
        print("Total Loan Outstanding:", loan_outstanding)


        value2 = self.get_text('//*[@id="DivIdToPrint"]/table[2]/tbody/tr[18]/th[5]/div')
        amount = (float(value2.replace(',', '')))
        print("Total Amount:", amount)

        value3 = self.get_text('//*[@id="DivIdToPrint"]/table[2]/tbody/tr[18]/th[6]/div')
        amount_current_month = float(value3.replace(',', ''))
        print("Total Loan Recovery Amount:", amount_current_month)


        exp_total_amount=loan_outstanding+amount-amount_current_month
        print("Expected Total Amount:", exp_total_amount)

        value4 = self.get_text('//*[@id="DivIdToPrint"]/table[2]/tbody/tr[18]/th[9]/div')
        act_total_amount = float(value4.replace(',', ''))
        print("Actual Total Amount:", act_total_amount)

        self.assert_equal(exp_total_amount, act_total_amount)

        if exp_total_amount==act_total_amount:
            print("Expected and Actual Amount Match")
        else:
            print("Expected and Actual Amount Don't Match")


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

        # PKSF POMIS-2 REPORT
        self.open_url("https://timf.imikrof.com/REPORT_PKSF_POMIS_2")
        self.type(report_level, "Branch")
        self.type(branch, "0062 - Pirgacha Branch")
        self.type(month, "March")
        self.click(show)

        self.wait(10)
        self.assert_text("POMIS-2 Report (with Service Charge)", "h2 div[align='center']")
        print("Report Open Successfully")

        # At the End of the Month  ( Borrower No )  (2+4)-7 = 8

        borrower1 = self.get_text('//*[@id="DivIdToPrint"]/table[2]/tbody/tr[18]/th[2]/div')
        print("Borrower No:", borrower1)

        borrower2 = self.get_text('//*[@id="DivIdToPrint"]/table[2]/tbody/tr[18]/th[4]/div')
        print("Borrower No:", borrower2)

        paid_borrower = self.get_text('//*[@id="DivIdToPrint"]/table[2]/tbody/tr[18]/th[7]')
        print("Paid Borrower:", paid_borrower)

        exp_total_borrower = str(int(borrower1) + int(borrower2) - int(paid_borrower))
        print("Expected Total Borrower:", exp_total_borrower)

        total_borrower = self.get_text('//*[@id="DivIdToPrint"]/table[2]/tbody/tr[18]/th[8]/div')
        print("Actual Total Borrower:", total_borrower)

        self.assert_equal(exp_total_borrower, total_borrower)

        if exp_total_borrower == total_borrower:
            print("Expected and Actual Borrower Match")
        else:
            print("Expected and Actual Borrower Doesn't Match")

        # At the End of the Month  ( Amount )   (3+5)-6 = 9

        value1 = self.get_text('//*[@id="DivIdToPrint"]/table[2]/tbody/tr[18]/th[3]/div')
        loan_outstanding = float(value1.replace(',', ''))
        print("Total Loan Outstanding:", loan_outstanding)

        value2 = self.get_text('//*[@id="DivIdToPrint"]/table[2]/tbody/tr[18]/th[5]/div')
        amount = (float(value2.replace(',', '')))
        print("Total Amount:", amount)

        value3 = self.get_text('//*[@id="DivIdToPrint"]/table[2]/tbody/tr[18]/th[6]/div')
        amount_current_month = float(value3.replace(',', ''))
        print("Total Loan Recovery Amount:", amount_current_month)

        exp_total_amount = loan_outstanding + amount - amount_current_month
        print("Expected Total Amount:", exp_total_amount)

        value4 = self.get_text('//*[@id="DivIdToPrint"]/table[2]/tbody/tr[18]/th[9]/div')
        act_total_amount = float(value4.replace(',', ''))
        print("Actual Total Amount:", act_total_amount)

        self.assert_equal(exp_total_amount, act_total_amount)

        if exp_total_amount == act_total_amount:
            print("Expected and Actual Amount Match")
        else:
            print("Expected and Actual Amount Don't Match")


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

        # PKSF POMIS-2 REPORT
        self.open_url("https://timf.imikrof.com/REPORT_PKSF_POMIS_2")
        self.type(report_level, "Branch")
        self.type(branch, "0061 - Khorkhori Branch")
        self.type(month, "March")
        self.click(show)

        self.wait(30)
        self.assert_text("POMIS-2 Report (with Service Charge)", "h2 div[align='center']")
        print("Report Open Successfully")

        # At the End of the Month  ( Borrower No )

        borrower1 = self.get_text('//*[@id="DivIdToPrint"]/table[2]/tbody/tr[18]/th[2]/div')
        print("Borrower No:", borrower1)

        borrower2 = self.get_text('//*[@id="DivIdToPrint"]/table[2]/tbody/tr[18]/th[4]/div')
        print("Borrower No:", borrower2)

        paid_borrower = self.get_text('//*[@id="DivIdToPrint"]/table[2]/tbody/tr[18]/th[7]')
        print("Paid Borrower:", paid_borrower)

        exp_total_borrower = str(int(borrower1) + int(borrower2) - int(paid_borrower))
        print("Expected Total Borrower:", exp_total_borrower)

        total_borrower = self.get_text('//*[@id="DivIdToPrint"]/table[2]/tbody/tr[18]/th[8]/div')
        print("Actual Total Borrower:", total_borrower)

        self.assert_equal(exp_total_borrower, total_borrower)

        if exp_total_borrower == total_borrower:
            print("Expected and Actual Borrower Match")
        else:
            print("Expected and Actual Borrower Doesn't Match")

        # At the End of the Month  ( Amount )  (3+5)-6 = 9

        value1 = self.get_text('//*[@id="DivIdToPrint"]/table[2]/tbody/tr[18]/th[3]/div')
        loan_outstanding = float(value1.replace(',', ''))
        print("Total Loan Outstanding:", loan_outstanding)

        value2 = self.get_text('//*[@id="DivIdToPrint"]/table[2]/tbody/tr[18]/th[5]/div')
        amount = (float(value2.replace(',', '')))
        print("Total Amount:", amount)

        value3 = self.get_text('//*[@id="DivIdToPrint"]/table[2]/tbody/tr[18]/th[6]/div')
        amount_current_month = float(value3.replace(',', ''))
        print("Total Loan Recovery Amount:", amount_current_month)

        exp_total_amount = loan_outstanding + amount - amount_current_month
        print("Expected Total Amount:", exp_total_amount)

        value4 = self.get_text('//*[@id="DivIdToPrint"]/table[2]/tbody/tr[18]/th[9]/div')
        act_total_amount = float(value4.replace(',', ''))
        print("Actual Total Amount:", act_total_amount)

        self.assert_equal(exp_total_amount, act_total_amount)

        if exp_total_amount == act_total_amount:
            print("Expected and Actual Amount Match")
        else:
            print("Expected and Actual Amount Don't Match")




























