from database.DB_connect import DBConnect
from model.retailer import Retailer


class DAO():
    def __init__(self):
        pass
    @staticmethod
    def getCountry():
        cnx=DBConnect.get_connection()
        cursor=cnx.cursor(dictionary=True)
        query="""select distinct r.Country
        from go_retailers r
        """
        cursor.execute(query)
        res=[]
        for row in cursor:
            res.append(row["Country"])
        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getYear():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select distinct year(g.Date) as year
            from go_daily_sales g
            """
        cursor.execute(query)
        res = []
        for row in cursor:
            res.append(row["year"])
        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getRetailers(country):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select r.*
                from go_retailers r
                where r.Country=%s
                """
        cursor.execute(query, (country,))
        res = []
        for row in cursor:
            res.append(Retailer(**row))
        cursor.close()
        cnx.close()
        return res


    @staticmethod
    def getArchi(country,anno):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select r1.Retailer_code rc1, r2.Retailer_code rc2, count(distinct r1.Product_number) as peso
from go_daily_sales  r1, go_daily_sales  r2, go_retailers r3, go_retailers r4
where r1.Product_number=r2.Product_number
and r1.Retailer_code < r2.Retailer_code
and r1.Retailer_code=r3.Retailer_code
and r2.Retailer_code=r4.Retailer_code  and r3.Country=%s and r4.Country=%s
and year(r1.Date) = year(r2.Date)
and year(r1.Date)=%s
group by r1.Retailer_code, r2.Retailer_code
                """
        cursor.execute(query, (country,country,anno))
        res = []
        for row in cursor:
            res.append((row["rc1"],row["rc2"],row["peso"]))
        cursor.close()
        cnx.close()
        return res
