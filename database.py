from sqlalchemy import create_engine,text

engine = create_engine("mysql+pymysql://root:Applem2air@127.0.0.1:3306/Project_manager?charset=utf8mb4")

if __name__=='__main__':
    with engine.connect() as conn:
        result = conn.execute(text("select * from Department;"))
        for i in result:
            print(i)