from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from datetime import date


db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'oogly-boogly'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)



    from .views import views
    from .auth import auth
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User

    create_database(app)
    seed_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        with app.app_context():
            db.create_all()
        print('Created Database!')


def seed_database(app):
    from .models import Gpu, Cpu, Motherboard, Ram, Storage, Psu, Case, Build
    with app.app_context():
        if not Gpu.query.first():  # Check if the Gpu table is empty
            # Add seed data for Gpu
            gpu1 = Gpu(gpu_name="Radeon RX 7900 XTX", manufacturer="PowerColor", gpu_brand="AMD", VRAM=12,
                       VRAM_type="GDDR5X", msrp=352, PCIe=5, ReleaseDate=date(2022, 3, 23))
            gpu2 = Gpu(gpu_name="GeForce RTX 2070 SuperGaming", manufacturer="XFX", gpu_brand="Nvidia", VRAM=8,
                       VRAM_type="GDDR5X", msrp=1647, PCIe=5, ReleaseDate=date(2023, 9, 24))
            gpu3 = Gpu(gpu_name="GeForce RTX 3090OC", manufacturer="Gigabyte", gpu_brand="Nvidia", VRAM=10,
                       VRAM_type="GDDR6", msrp=515, PCIe=5, ReleaseDate=date(2020, 10, 16))
            gpu4 = Gpu(gpu_name="GeForce RTX 2080 TiUltra", manufacturer="PowerColor", gpu_brand="Nvidia", VRAM=16,
                       VRAM_type="GDDR6X", msrp=1781, PCIe=5, ReleaseDate=date(2018, 9, 3))
            gpu5 = Gpu(gpu_name="GeForce RTX 2080Gaming", manufacturer="PowerColor", gpu_brand="Nvidia", VRAM=8,
                       VRAM_type="GDDR5", msrp=1101, PCIe=5, ReleaseDate=date(2024, 10, 18))
            gpu6 = Gpu(gpu_name="Radeon RX 6700 XTGaming", manufacturer="Sapphire", gpu_brand="AMD", VRAM=10,
                       VRAM_type="GDDR6", msrp=1279, PCIe=4, ReleaseDate=date(2022, 12, 2))
            gpu7 = Gpu(gpu_name="GeForce RTX 2080 TiGaming", manufacturer="Gigabyte", gpu_brand="Nvidia", VRAM=24,
                       VRAM_type="GDDR5", msrp=1246, PCIe=4, ReleaseDate=date(2021, 12, 15))
            gpu8 = Gpu(gpu_name="ARC A750", manufacturer="XFX", gpu_brand="Intel", VRAM=12, VRAM_type="GDDR5X",
                       msrp=1056, PCIe=4, ReleaseDate=date(2022, 6, 25))
            gpu9 = Gpu(gpu_name="Radeon RX 6700 XT", manufacturer="EVGA", gpu_brand="AMD", VRAM=6, VRAM_type="GDDR5X",
                       msrp=274, PCIe=5, ReleaseDate=date(2020, 9, 25))
            gpu10 = Gpu(gpu_name="GeForce RTX 2070 SuperOC", manufacturer="XFX", gpu_brand="Nvidia", VRAM=6,
                        VRAM_type="GDDR5", msrp=682, PCIe=4, ReleaseDate=date(2019, 8, 25))
            gpu11 = Gpu(gpu_name="GeForce RTX 2070 SuperX", manufacturer="MSI", gpu_brand="Nvidia", VRAM=6,
                        VRAM_type="GDDR5X", msrp=1415, PCIe=3, ReleaseDate=date(2019, 4, 22))
            gpu12 = Gpu(gpu_name="ARC A750X", manufacturer="MSI", gpu_brand="Intel", VRAM=24, VRAM_type="GDDR6X",
                        msrp=1323, PCIe=3, ReleaseDate=date(2018, 4, 23))
            gpu13 = Gpu(gpu_name="GeForce RTX 3090X", manufacturer="XFX", gpu_brand="Nvidia", VRAM=12,
                        VRAM_type="GDDR6", msrp=1793, PCIe=4, ReleaseDate=date(2019, 2, 20))
            gpu14 = Gpu(gpu_name="GeForce RTX 3090Gaming", manufacturer="Zotac", gpu_brand="Nvidia", VRAM=16,
                        VRAM_type="GDDR6X", msrp=617, PCIe=4, ReleaseDate=date(2019, 11, 4))
            gpu15 = Gpu(gpu_name="Radeon RX 7900 XTXGaming", manufacturer="MSI", gpu_brand="AMD", VRAM=16,
                        VRAM_type="GDDR5X", msrp=1311, PCIe=5, ReleaseDate=date(2023, 10, 26))
            gpu16 = Gpu(gpu_name="GeForce RTX 3070X", manufacturer="PowerColor", gpu_brand="Nvidia", VRAM=10,
                        VRAM_type="GDDR5", msrp=1490, PCIe=5, ReleaseDate=date(2020, 6, 9))
            gpu17 = Gpu(gpu_name="GeForce RTX 2070 SuperOC", manufacturer="EVGA", gpu_brand="Nvidia", VRAM=16,
                        VRAM_type="GDDR5", msrp=715, PCIe=3, ReleaseDate=date(2022, 7, 6))
            gpu18 = Gpu(gpu_name="GeForce RTX 2080 TiUltra", manufacturer="Zotac", gpu_brand="Nvidia", VRAM=12,
                        VRAM_type="GDDR5", msrp=385, PCIe=5, ReleaseDate=date(2023, 11, 5))
            gpu19 = Gpu(gpu_name="GeForce RTX 2080Ultra", manufacturer="Sapphire", gpu_brand="Nvidia", VRAM=10,
                        VRAM_type="GDDR5X", msrp=1439, PCIe=5, ReleaseDate=date(2021, 1, 17))
            gpu20 = Gpu(gpu_name="ARC A770", manufacturer="PowerColor", gpu_brand="Intel", VRAM=12, VRAM_type="GDDR6",
                        msrp=1300, PCIe=5, ReleaseDate=date(2019, 10, 22))
            gpu21 = Gpu(gpu_name="GeForce RTX 3090Gaming", manufacturer="ASUS", gpu_brand="Nvidia", VRAM=6,
                        VRAM_type="GDDR5X", msrp=582, PCIe=4, ReleaseDate=date(2022, 7, 14))
            gpu22 = Gpu(gpu_name="Radeon RX 7900 XTX", manufacturer="PowerColor", gpu_brand="AMD", VRAM=6,
                        VRAM_type="GDDR6X", msrp=429, PCIe=3, ReleaseDate=date(2024, 10, 1))
            gpu23 = Gpu(gpu_name="GeForce RTX 2080Gaming", manufacturer="Sapphire", gpu_brand="Nvidia", VRAM=6,
                        VRAM_type="GDDR5X", msrp=411, PCIe=3, ReleaseDate=date(2020, 4, 24))
            gpu24 = Gpu(gpu_name="GeForce RTX 3080X", manufacturer="XFX", gpu_brand="Nvidia", VRAM=16,
                        VRAM_type="GDDR6", msrp=827, PCIe=3, ReleaseDate=date(2018, 10, 10))
            gpu25 = Gpu(gpu_name="ARC A770OC", manufacturer="Sapphire", gpu_brand="Intel", VRAM=12, VRAM_type="GDDR6",
                        msrp=1430, PCIe=4, ReleaseDate=date(2021, 3, 16))
            gpu26 = Gpu(gpu_name="GeForce RTX 2070 Super", manufacturer="ASUS", gpu_brand="Nvidia", VRAM=10,
                        VRAM_type="GDDR5X", msrp=728, PCIe=5, ReleaseDate=date(2020, 3, 16))
            gpu27 = Gpu(gpu_name="GeForce RTX 4090OC", manufacturer="ASUS", gpu_brand="Nvidia", VRAM=24,
                        VRAM_type="GDDR5", msrp=1623, PCIe=5, ReleaseDate=date(2020, 11, 18))
            gpu28 = Gpu(gpu_name="Radeon RX 7900 XTXGaming", manufacturer="Sapphire", gpu_brand="AMD", VRAM=8,
                        VRAM_type="GDDR6", msrp=1661, PCIe=4, ReleaseDate=date(2024, 12, 25))
            gpu29 = Gpu(gpu_name="GeForce RTX 4090", manufacturer="EVGA", gpu_brand="Nvidia", VRAM=10,
                        VRAM_type="GDDR6", msrp=651, PCIe=3, ReleaseDate=date(2020, 9, 7))
            gpu30 = Gpu(gpu_name="GeForce RTX 2080 TiOC", manufacturer="EVGA", gpu_brand="Nvidia", VRAM=8,
                        VRAM_type="GDDR5", msrp=1165, PCIe=5, ReleaseDate=date(2019, 11, 2))
            gpu31 = Gpu(gpu_name="GeForce RTX 3080X", manufacturer="Sapphire", gpu_brand="Nvidia", VRAM=24,
                        VRAM_type="GDDR6", msrp=1234, PCIe=4, ReleaseDate=date(2021, 6, 27))
            gpu32 = Gpu(gpu_name="Radeon RX 6800Gaming", manufacturer="EVGA", gpu_brand="AMD", VRAM=6,
                        VRAM_type="GDDR6X", msrp=722, PCIe=3, ReleaseDate=date(2024, 4, 25))
            gpu33 = Gpu(gpu_name="GeForce RTX 4090OC", manufacturer="MSI", gpu_brand="Nvidia", VRAM=16,
                        VRAM_type="GDDR6", msrp=1090, PCIe=4, ReleaseDate=date(2019, 6, 5))
            gpu34 = Gpu(gpu_name="GeForce RTX 3090Gaming", manufacturer="Zotac", gpu_brand="Nvidia", VRAM=6,
                        VRAM_type="GDDR6", msrp=834, PCIe=5, ReleaseDate=date(2020, 2, 12))
            gpu35 = Gpu(gpu_name="GeForce RTX 4070Ultra", manufacturer="Gigabyte", gpu_brand="Nvidia", VRAM=16,
                        VRAM_type="GDDR6X", msrp=1739, PCIe=3, ReleaseDate=date(2022, 9, 18))
            gpu36 = Gpu(gpu_name="Radeon RX 6700 XTUltra", manufacturer="PowerColor", gpu_brand="AMD", VRAM=16,
                        VRAM_type="GDDR5X", msrp=1209, PCIe=5, ReleaseDate=date(2018, 2, 2))
            gpu37 = Gpu(gpu_name="GeForce RTX 4070OC", manufacturer="Gigabyte", gpu_brand="Nvidia", VRAM=10,
                        VRAM_type="GDDR5X", msrp=1435, PCIe=4, ReleaseDate=date(2024, 9, 22))
            gpu38 = Gpu(gpu_name="Radeon RX 6700 XTOC", manufacturer="MSI", gpu_brand="AMD", VRAM=12,
                        VRAM_type="GDDR6X", msrp=338, PCIe=3, ReleaseDate=date(2020, 12, 25))
            gpu39 = Gpu(gpu_name="GeForce RTX 2080 Ti", manufacturer="Gigabyte", gpu_brand="Nvidia", VRAM=6,
                        VRAM_type="GDDR5", msrp=653, PCIe=4, ReleaseDate=date(2018, 3, 26))
            gpu40 = Gpu(gpu_name="Radeon RX 7900 XTX", manufacturer="XFX", gpu_brand="AMD", VRAM=16, VRAM_type="GDDR5",
                        msrp=673, PCIe=5, ReleaseDate=date(2024, 7, 1))
            gpu41 = Gpu(gpu_name="GeForce RTX 3070Ultra", manufacturer="PowerColor", gpu_brand="Nvidia", VRAM=8,
                        VRAM_type="GDDR5X", msrp=1050, PCIe=3, ReleaseDate=date(2021, 8, 3))
            gpu42 = Gpu(gpu_name="Radeon RX 7900 XTX", manufacturer="EVGA", gpu_brand="AMD", VRAM=12, VRAM_type="GDDR5",
                        msrp=1482, PCIe=3, ReleaseDate=date(2019, 3, 21))
            gpu43 = Gpu(gpu_name="Radeon RX 5700 XTUltra", manufacturer="PowerColor", gpu_brand="AMD", VRAM=24,
                        VRAM_type="GDDR6", msrp=1048, PCIe=4, ReleaseDate=date(2018, 1, 19))
            gpu44 = Gpu(gpu_name="GeForce RTX 3080Ultra", manufacturer="EVGA", gpu_brand="Nvidia", VRAM=6,
                        VRAM_type="GDDR6X", msrp=1497, PCIe=4, ReleaseDate=date(2023, 5, 20))
            gpu45 = Gpu(gpu_name="GeForce RTX 2070 Super", manufacturer="PowerColor", gpu_brand="Nvidia", VRAM=6,
                        VRAM_type="GDDR5X", msrp=431, PCIe=3, ReleaseDate=date(2019, 7, 21))
            gpu46 = Gpu(gpu_name="ARC A750Gaming", manufacturer="Sapphire", gpu_brand="Intel", VRAM=10,
                        VRAM_type="GDDR6X", msrp=1361, PCIe=3, ReleaseDate=date(2023, 6, 26))
            gpu47 = Gpu(gpu_name="GeForce RTX 3090", manufacturer="XFX", gpu_brand="Nvidia", VRAM=16, VRAM_type="GDDR5",
                        msrp=441, PCIe=3, ReleaseDate=date(2023, 6, 8))
            gpu48 = Gpu(gpu_name="GeForce RTX 3070", manufacturer="XFX", gpu_brand="Nvidia", VRAM=6, VRAM_type="GDDR6",
                        msrp=1357, PCIe=5, ReleaseDate=date(2019, 4, 18))
            gpu49 = Gpu(gpu_name="Radeon RX 6800X", manufacturer="ASUS", gpu_brand="AMD", VRAM=10, VRAM_type="GDDR6",
                        msrp=736, PCIe=4, ReleaseDate=date(2018, 1, 6))
            gpu50 = Gpu(gpu_name="GeForce RTX 2080 TiUltra", manufacturer="Gigabyte", gpu_brand="Nvidia", VRAM=16,
                        VRAM_type="GDDR6", msrp=661, PCIe=3, ReleaseDate=date(2024, 12, 6))
            gpu51 = Gpu(gpu_name="Radeon RX 6700 XT", manufacturer="Zotac", gpu_brand="AMD", VRAM=16, VRAM_type="GDDR5",
                        msrp=953, PCIe=3, ReleaseDate=date(2023, 12, 20))
            gpu52 = Gpu(gpu_name="GeForce RTX 4070Gaming", manufacturer="Zotac", gpu_brand="Nvidia", VRAM=24,
                        VRAM_type="GDDR6X", msrp=973, PCIe=4, ReleaseDate=date(2018, 3, 10))
            gpu53 = Gpu(gpu_name="GeForce RTX 4070OC", manufacturer="Gigabyte", gpu_brand="Nvidia", VRAM=16,
                        VRAM_type="GDDR6", msrp=616, PCIe=3, ReleaseDate=date(2021, 11, 4))
            gpu54 = Gpu(gpu_name="GeForce RTX 2080 TiGaming", manufacturer="Gigabyte", gpu_brand="Nvidia", VRAM=6,
                        VRAM_type="GDDR5X", msrp=1324, PCIe=4, ReleaseDate=date(2020, 12, 19))
            gpu55 = Gpu(gpu_name="GeForce RTX 2070 SuperOC", manufacturer="Gigabyte", gpu_brand="Nvidia", VRAM=24,
                        VRAM_type="GDDR5", msrp=1008, PCIe=4, ReleaseDate=date(2020, 8, 16))
            gpu56 = Gpu(gpu_name="GeForce RTX 4070OC", manufacturer="Zotac", gpu_brand="Nvidia", VRAM=16,
                        VRAM_type="GDDR5X", msrp=1603, PCIe=5, ReleaseDate=date(2018, 7, 13))
            gpu57 = Gpu(gpu_name="GeForce RTX 4090X", manufacturer="MSI", gpu_brand="Nvidia", VRAM=16,
                        VRAM_type="GDDR6", msrp=969, PCIe=3, ReleaseDate=date(2022, 11, 14))
            gpu58 = Gpu(gpu_name="GeForce RTX 4070Gaming", manufacturer="Gigabyte", gpu_brand="Nvidia", VRAM=16,
                        VRAM_type="GDDR6X", msrp=228, PCIe=4, ReleaseDate=date(2018, 3, 25))
            gpu59 = Gpu(gpu_name="Radeon RX 5700 XTX", manufacturer="ASUS", gpu_brand="AMD", VRAM=24,
                        VRAM_type="GDDR6X", msrp=812, PCIe=5, ReleaseDate=date(2022, 11, 15))
            gpu60 = Gpu(gpu_name="GeForce RTX 2080 Ti", manufacturer="Sapphire", gpu_brand="Nvidia", VRAM=16,
                        VRAM_type="GDDR5X", msrp=793, PCIe=4, ReleaseDate=date(2021, 11, 18))
            gpu61 = Gpu(gpu_name="ARC A750Gaming", manufacturer="MSI", gpu_brand="Intel", VRAM=8, VRAM_type="GDDR5X",
                        msrp=800, PCIe=4, ReleaseDate=date(2022, 8, 16))
            gpu62 = Gpu(gpu_name="GeForce RTX 2070 Super", manufacturer="XFX", gpu_brand="Nvidia", VRAM=10,
                        VRAM_type="GDDR5", msrp=1624, PCIe=5, ReleaseDate=date(2020, 3, 3))
            gpu63 = Gpu(gpu_name="GeForce RTX 3080X", manufacturer="MSI", gpu_brand="Nvidia", VRAM=24,
                        VRAM_type="GDDR5X", msrp=440, PCIe=3, ReleaseDate=date(2024, 3, 3))
            gpu64 = Gpu(gpu_name="GeForce RTX 3090Ultra", manufacturer="PowerColor", gpu_brand="Nvidia", VRAM=24,
                        VRAM_type="GDDR5", msrp=1762, PCIe=3, ReleaseDate=date(2020, 5, 3))
            gpu65 = Gpu(gpu_name="Radeon RX 6800", manufacturer="Sapphire", gpu_brand="AMD", VRAM=10, VRAM_type="GDDR5",
                        msrp=406, PCIe=5, ReleaseDate=date(2024, 3, 22))
            gpu66 = Gpu(gpu_name="Radeon RX 6800OC", manufacturer="MSI", gpu_brand="AMD", VRAM=6, VRAM_type="GDDR5X",
                        msrp=1357, PCIe=5, ReleaseDate=date(2022, 10, 14))
            gpu67 = Gpu(gpu_name="Radeon RX 6700 XTUltra", manufacturer="MSI", gpu_brand="AMD", VRAM=24,
                        VRAM_type="GDDR6", msrp=373, PCIe=4, ReleaseDate=date(2021, 9, 22))
            gpu68 = Gpu(gpu_name="Radeon RX 6800Gaming", manufacturer="MSI", gpu_brand="AMD", VRAM=6, VRAM_type="GDDR5",
                        msrp=1741, PCIe=4, ReleaseDate=date(2024, 7, 17))
            gpu69 = Gpu(gpu_name="Radeon RX 6700 XTUltra", manufacturer="ASUS", gpu_brand="AMD", VRAM=12,
                        VRAM_type="GDDR6", msrp=846, PCIe=4, ReleaseDate=date(2020, 11, 5))
            gpu70 = Gpu(gpu_name="Radeon RX 6700 XT", manufacturer="ASUS", gpu_brand="AMD", VRAM=6, VRAM_type="GDDR5X",
                        msrp=458, PCIe=4, ReleaseDate=date(2020, 11, 16))
            gpu71 = Gpu(gpu_name="Radeon RX 6700 XTOC", manufacturer="ASUS", gpu_brand="AMD", VRAM=10,
                        VRAM_type="GDDR6", msrp=1451, PCIe=4, ReleaseDate=date(2023, 10, 4))
            gpu72 = Gpu(gpu_name="GeForce RTX 3080OC", manufacturer="XFX", gpu_brand="Nvidia", VRAM=10,
                        VRAM_type="GDDR6", msrp=1126, PCIe=3, ReleaseDate=date(2024, 4, 22))
            gpu73 = Gpu(gpu_name="GeForce RTX 4070Gaming", manufacturer="MSI", gpu_brand="Nvidia", VRAM=6,
                        VRAM_type="GDDR5X", msrp=1129, PCIe=4, ReleaseDate=date(2022, 6, 8))
            gpu74 = Gpu(gpu_name="ARC A750X", manufacturer="EVGA", gpu_brand="Intel", VRAM=16, VRAM_type="GDDR5",
                        msrp=1232, PCIe=5, ReleaseDate=date(2018, 12, 28))
            gpu75 = Gpu(gpu_name="ARC A750OC", manufacturer="PowerColor", gpu_brand="Intel", VRAM=8, VRAM_type="GDDR5X",
                        msrp=622, PCIe=4, ReleaseDate=date(2024, 11, 20))
            gpu76 = Gpu(gpu_name="ARC A770OC", manufacturer="Sapphire", gpu_brand="Intel", VRAM=8, VRAM_type="GDDR5X",
                        msrp=1715, PCIe=4, ReleaseDate=date(2023, 4, 16))
            gpu77 = Gpu(gpu_name="GeForce RTX 3070OC", manufacturer="MSI", gpu_brand="Nvidia", VRAM=24,
                        VRAM_type="GDDR5", msrp=1600, PCIe=3, ReleaseDate=date(2018, 3, 11))
            gpu78 = Gpu(gpu_name="Radeon RX 6800OC", manufacturer="Sapphire", gpu_brand="AMD", VRAM=6,
                        VRAM_type="GDDR6", msrp=632, PCIe=5, ReleaseDate=date(2019, 10, 19))
            gpu79 = Gpu(gpu_name="Radeon RX 6700 XT", manufacturer="MSI", gpu_brand="AMD", VRAM=8, VRAM_type="GDDR5X",
                        msrp=210, PCIe=3, ReleaseDate=date(2023, 4, 18))
            gpu80 = Gpu(gpu_name="Radeon RX 6800Gaming", manufacturer="Zotac", gpu_brand="AMD", VRAM=16,
                        VRAM_type="GDDR6X", msrp=585, PCIe=4, ReleaseDate=date(2019, 1, 4))
            gpu81 = Gpu(gpu_name="GeForce RTX 3070", manufacturer="Sapphire", gpu_brand="Nvidia", VRAM=24,
                        VRAM_type="GDDR6", msrp=1294, PCIe=5, ReleaseDate=date(2024, 3, 13))
            gpu82 = Gpu(gpu_name="GeForce RTX 2080 TiGaming", manufacturer="MSI", gpu_brand="Nvidia", VRAM=10,
                        VRAM_type="GDDR5X", msrp=326, PCIe=4, ReleaseDate=date(2024, 3, 3))
            gpu83 = Gpu(gpu_name="ARC A770", manufacturer="PowerColor", gpu_brand="Intel", VRAM=12, VRAM_type="GDDR5",
                        msrp=1668, PCIe=5, ReleaseDate=date(2020, 7, 26))
            gpu84 = Gpu(gpu_name="GeForce RTX 2080 TiOC", manufacturer="Sapphire", gpu_brand="Nvidia", VRAM=24,
                        VRAM_type="GDDR6", msrp=1538, PCIe=3, ReleaseDate=date(2024, 5, 22))
            gpu85 = Gpu(gpu_name="GeForce RTX 2070 SuperX", manufacturer="MSI", gpu_brand="Nvidia", VRAM=16,
                        VRAM_type="GDDR5X", msrp=1574, PCIe=3, ReleaseDate=date(2023, 4, 16))
            gpu86 = Gpu(gpu_name="Radeon RX 5700 XTUltra", manufacturer="Zotac", gpu_brand="AMD", VRAM=6,
                        VRAM_type="GDDR6X", msrp=1006, PCIe=3, ReleaseDate=date(2019, 8, 5))
            gpu87 = Gpu(gpu_name="Radeon RX 5700 XTGaming", manufacturer="MSI", gpu_brand="AMD", VRAM=10,
                        VRAM_type="GDDR6", msrp=1745, PCIe=5, ReleaseDate=date(2018, 3, 24))
            gpu88 = Gpu(gpu_name="GeForce RTX 3070Gaming", manufacturer="Sapphire", gpu_brand="Nvidia", VRAM=12,
                        VRAM_type="GDDR5X", msrp=1629, PCIe=3, ReleaseDate=date(2023, 9, 16))
            gpu89 = Gpu(gpu_name="GeForce RTX 2070 Super", manufacturer="PowerColor", gpu_brand="Nvidia", VRAM=16,
                        VRAM_type="GDDR6", msrp=984, PCIe=4, ReleaseDate=date(2024, 3, 21))
            gpu90 = Gpu(gpu_name="GeForce RTX 3080OC", manufacturer="Zotac", gpu_brand="Nvidia", VRAM=10,
                        VRAM_type="GDDR5", msrp=305, PCIe=5, ReleaseDate=date(2023, 7, 16))
            gpu91 = Gpu(gpu_name="GeForce RTX 3080OC", manufacturer="PowerColor", gpu_brand="Nvidia", VRAM=16,
                        VRAM_type="GDDR6", msrp=782, PCIe=4, ReleaseDate=date(2021, 3, 26))
            gpu92 = Gpu(gpu_name="GeForce RTX 4090Gaming", manufacturer="ASUS", gpu_brand="Nvidia", VRAM=8,
                        VRAM_type="GDDR6", msrp=1551, PCIe=3, ReleaseDate=date(2019, 12, 14))
            gpu93 = Gpu(gpu_name="Radeon RX 7900 XTX", manufacturer="EVGA", gpu_brand="AMD", VRAM=12, VRAM_type="GDDR6",
                        msrp=916, PCIe=4, ReleaseDate=date(2018, 10, 13))
            gpu94 = Gpu(gpu_name="ARC A750", manufacturer="Gigabyte", gpu_brand="Intel", VRAM=24, VRAM_type="GDDR6X",
                        msrp=275, PCIe=4, ReleaseDate=date(2024, 1, 12))
            gpu95 = Gpu(gpu_name="GeForce RTX 3080Gaming", manufacturer="MSI", gpu_brand="Nvidia", VRAM=10,
                        VRAM_type="GDDR6X", msrp=757, PCIe=4, ReleaseDate=date(2019, 10, 24))
            gpu96 = Gpu(gpu_name="GeForce RTX 4090Gaming", manufacturer="XFX", gpu_brand="Nvidia", VRAM=16,
                        VRAM_type="GDDR6X", msrp=694, PCIe=4, ReleaseDate=date(2023, 12, 17))
            gpu97 = Gpu(gpu_name="GeForce RTX 3090Ultra", manufacturer="XFX", gpu_brand="Nvidia", VRAM=10,
                        VRAM_type="GDDR6X", msrp=394, PCIe=5, ReleaseDate=date(2020, 12, 23))
            gpu98 = Gpu(gpu_name="GeForce RTX 3070", manufacturer="Zotac", gpu_brand="Nvidia", VRAM=6,
                        VRAM_type="GDDR6", msrp=1540, PCIe=4, ReleaseDate=date(2021, 1, 14))
            gpu99 = Gpu(gpu_name="GeForce RTX 3080X", manufacturer="Gigabyte", gpu_brand="Nvidia", VRAM=24,
                        VRAM_type="GDDR6X", msrp=926, PCIe=4, ReleaseDate=date(2020, 2, 10))
            gpu100 = Gpu(gpu_name="Radeon RX 5700 XTX", manufacturer="Gigabyte", gpu_brand="AMD", VRAM=16,
                         VRAM_type="GDDR6", msrp=1669, PCIe=4, ReleaseDate=date(2023, 9, 1))
            gpu101 = Gpu(gpu_name="GeForce RTX 2080 TiGaming", manufacturer="MSI", gpu_brand="Nvidia", VRAM=10,
                         VRAM_type="GDDR5X", msrp=1714, PCIe=3, ReleaseDate=date(2020, 7, 16))
            gpu102 = Gpu(gpu_name="Radeon RX 6800X", manufacturer="Sapphire", gpu_brand="AMD", VRAM=16,
                         VRAM_type="GDDR6X", msrp=318, PCIe=4, ReleaseDate=date(2023, 5, 15))
            gpu103 = Gpu(gpu_name="GeForce RTX 3090Gaming", manufacturer="Zotac", gpu_brand="Nvidia", VRAM=8,
                         VRAM_type="GDDR5", msrp=1024, PCIe=4, ReleaseDate=date(2022, 5, 5))
            gpu104 = Gpu(gpu_name="ARC A750Ultra", manufacturer="Gigabyte", gpu_brand="Intel", VRAM=10,
                         VRAM_type="GDDR5X", msrp=1783, PCIe=3, ReleaseDate=date(2019, 7, 11))
            gpu105 = Gpu(gpu_name="GeForce RTX 4090X", manufacturer="MSI", gpu_brand="Nvidia", VRAM=12,
                         VRAM_type="GDDR6", msrp=1333, PCIe=5, ReleaseDate=date(2019, 8, 8))
            gpu106 = Gpu(gpu_name="GeForce RTX 3070OC", manufacturer="Zotac", gpu_brand="Nvidia", VRAM=10,
                         VRAM_type="GDDR6", msrp=1626, PCIe=5, ReleaseDate=date(2023, 5, 20))
            gpu107 = Gpu(gpu_name="GeForce RTX 4090X", manufacturer="ASUS", gpu_brand="Nvidia", VRAM=16,
                         VRAM_type="GDDR6", msrp=972, PCIe=5, ReleaseDate=date(2024, 10, 15))
            gpu108 = Gpu(gpu_name="Radeon RX 6800X", manufacturer="Gigabyte", gpu_brand="AMD", VRAM=16,
                         VRAM_type="GDDR6", msrp=886, PCIe=3, ReleaseDate=date(2022, 11, 28))
            gpu109 = Gpu(gpu_name="GeForce RTX 2080Ultra", manufacturer="XFX", gpu_brand="Nvidia", VRAM=12,
                         VRAM_type="GDDR5X", msrp=627, PCIe=5, ReleaseDate=date(2023, 9, 22))
            gpu110 = Gpu(gpu_name="GeForce RTX 4070Gaming", manufacturer="MSI", gpu_brand="Nvidia", VRAM=12,
                         VRAM_type="GDDR6X", msrp=1097, PCIe=4, ReleaseDate=date(2020, 5, 23))
            gpu111 = Gpu(gpu_name="GeForce RTX 3090OC", manufacturer="Zotac", gpu_brand="Nvidia", VRAM=6,
                         VRAM_type="GDDR6", msrp=1023, PCIe=5, ReleaseDate=date(2022, 7, 4))
            gpu112 = Gpu(gpu_name="GeForce RTX 3070", manufacturer="Sapphire", gpu_brand="Nvidia", VRAM=16,
                         VRAM_type="GDDR6X", msrp=465, PCIe=3, ReleaseDate=date(2019, 3, 6))
            gpu113 = Gpu(gpu_name="GeForce RTX 2080Ultra", manufacturer="Zotac", gpu_brand="Nvidia", VRAM=12,
                         VRAM_type="GDDR6X", msrp=1025, PCIe=4, ReleaseDate=date(2022, 7, 26))
            gpu114 = Gpu(gpu_name="Radeon RX 6700 XTX", manufacturer="Sapphire", gpu_brand="AMD", VRAM=8,
                         VRAM_type="GDDR6", msrp=1106, PCIe=5, ReleaseDate=date(2020, 6, 8))
            gpu115 = Gpu(gpu_name="GeForce RTX 3080Ultra", manufacturer="Zotac", gpu_brand="Nvidia", VRAM=6,
                         VRAM_type="GDDR6", msrp=1594, PCIe=3, ReleaseDate=date(2022, 1, 20))
            gpu116 = Gpu(gpu_name="Radeon RX 7900 XTXX", manufacturer="EVGA", gpu_brand="AMD", VRAM=12,
                         VRAM_type="GDDR6", msrp=269, PCIe=5, ReleaseDate=date(2023, 5, 16))
            gpu117 = Gpu(gpu_name="GeForce RTX 2080OC", manufacturer="MSI", gpu_brand="Nvidia", VRAM=10,
                         VRAM_type="GDDR5X", msrp=1355, PCIe=5, ReleaseDate=date(2020, 7, 1))
            gpu118 = Gpu(gpu_name="GeForce RTX 2080 TiUltra", manufacturer="Sapphire", gpu_brand="Nvidia", VRAM=12,
                         VRAM_type="GDDR6", msrp=1396, PCIe=4, ReleaseDate=date(2019, 11, 17))
            gpu119 = Gpu(gpu_name="GeForce RTX 3070", manufacturer="Sapphire", gpu_brand="Nvidia", VRAM=10,
                         VRAM_type="GDDR5", msrp=1626, PCIe=5, ReleaseDate=date(2022, 12, 15))
            gpu120 = Gpu(gpu_name="GeForce RTX 4070", manufacturer="Sapphire", gpu_brand="Nvidia", VRAM=24,
                         VRAM_type="GDDR6X", msrp=1009, PCIe=5, ReleaseDate=date(2022, 11, 3))
            gpu121 = Gpu(gpu_name="ARC A770OC", manufacturer="XFX", gpu_brand="Intel", VRAM=6, VRAM_type="GDDR5",
                         msrp=998, PCIe=5, ReleaseDate=date(2018, 7, 26))
            gpu122 = Gpu(gpu_name="Radeon RX 5700 XTUltra", manufacturer="Sapphire", gpu_brand="AMD", VRAM=12,
                         VRAM_type="GDDR5X", msrp=204, PCIe=3, ReleaseDate=date(2019, 5, 7))
            gpu123 = Gpu(gpu_name="GeForce RTX 2080X", manufacturer="ASUS", gpu_brand="Nvidia", VRAM=16,
                         VRAM_type="GDDR5X", msrp=629, PCIe=5, ReleaseDate=date(2020, 4, 19))
            gpu124 = Gpu(gpu_name="Radeon RX 7900 XTXX", manufacturer="Zotac", gpu_brand="AMD", VRAM=16,
                         VRAM_type="GDDR6", msrp=919, PCIe=4, ReleaseDate=date(2021, 11, 21))
            gpu125 = Gpu(gpu_name="Radeon RX 6700 XTGaming", manufacturer="Zotac", gpu_brand="AMD", VRAM=12,
                         VRAM_type="GDDR5X", msrp=1242, PCIe=3, ReleaseDate=date(2022, 7, 19))
            gpu126 = Gpu(gpu_name="Radeon RX 5700 XTGaming", manufacturer="EVGA", gpu_brand="AMD", VRAM=10,
                         VRAM_type="GDDR5X", msrp=1201, PCIe=5, ReleaseDate=date(2021, 9, 23))
            gpu127 = Gpu(gpu_name="GeForce RTX 4090", manufacturer="EVGA", gpu_brand="Nvidia", VRAM=8,
                         VRAM_type="GDDR6X", msrp=553, PCIe=4, ReleaseDate=date(2024, 12, 28))
            gpu128 = Gpu(gpu_name="Radeon RX 6700 XTUltra", manufacturer="XFX", gpu_brand="AMD", VRAM=16,
                         VRAM_type="GDDR5X", msrp=1496, PCIe=3, ReleaseDate=date(2020, 6, 11))
            gpu129 = Gpu(gpu_name="GeForce RTX 2070 SuperGaming", manufacturer="Zotac", gpu_brand="Nvidia", VRAM=8,
                         VRAM_type="GDDR5X", msrp=749, PCIe=4, ReleaseDate=date(2022, 8, 28))
            gpu130 = Gpu(gpu_name="Radeon RX 6700 XTUltra", manufacturer="Sapphire", gpu_brand="AMD", VRAM=6,
                         VRAM_type="GDDR5", msrp=1025, PCIe=4, ReleaseDate=date(2018, 8, 1))
            gpu131 = Gpu(gpu_name="GeForce RTX 3070Gaming", manufacturer="PowerColor", gpu_brand="Nvidia", VRAM=12,
                         VRAM_type="GDDR6", msrp=333, PCIe=3, ReleaseDate=date(2022, 3, 20))
            gpu132 = Gpu(gpu_name="GeForce RTX 3090Gaming", manufacturer="PowerColor", gpu_brand="Nvidia", VRAM=24,
                         VRAM_type="GDDR6", msrp=1395, PCIe=3, ReleaseDate=date(2018, 7, 21))
            gpu133 = Gpu(gpu_name="GeForce RTX 3080Ultra", manufacturer="ASUS", gpu_brand="Nvidia", VRAM=12,
                         VRAM_type="GDDR6X", msrp=1765, PCIe=3, ReleaseDate=date(2019, 5, 11))
            gpu134 = Gpu(gpu_name="GeForce RTX 2080Gaming", manufacturer="MSI", gpu_brand="Nvidia", VRAM=12,
                         VRAM_type="GDDR5", msrp=1402, PCIe=4, ReleaseDate=date(2020, 12, 27))
            gpu135 = Gpu(gpu_name="Radeon RX 7900 XTXGaming", manufacturer="XFX", gpu_brand="AMD", VRAM=12,
                         VRAM_type="GDDR6", msrp=1164, PCIe=3, ReleaseDate=date(2018, 4, 23))
            gpu136 = Gpu(gpu_name="Radeon RX 6800Gaming", manufacturer="Gigabyte", gpu_brand="AMD", VRAM=12,
                         VRAM_type="GDDR5X", msrp=467, PCIe=3, ReleaseDate=date(2024, 9, 15))
            gpu137 = Gpu(gpu_name="GeForce RTX 2070 SuperOC", manufacturer="PowerColor", gpu_brand="Nvidia", VRAM=12,
                         VRAM_type="GDDR5", msrp=571, PCIe=5, ReleaseDate=date(2022, 6, 10))
            gpu138 = Gpu(gpu_name="ARC A750OC", manufacturer="ASUS", gpu_brand="Intel", VRAM=8, VRAM_type="GDDR5X",
                         msrp=1694, PCIe=4, ReleaseDate=date(2024, 5, 8))
            gpu139 = Gpu(gpu_name="GeForce RTX 4090", manufacturer="ASUS", gpu_brand="Nvidia", VRAM=10,
                         VRAM_type="GDDR5X", msrp=1322, PCIe=5, ReleaseDate=date(2020, 12, 23))
            gpu140 = Gpu(gpu_name="GeForce RTX 2070 Super", manufacturer="Zotac", gpu_brand="Nvidia", VRAM=8,
                         VRAM_type="GDDR6", msrp=1007, PCIe=3, ReleaseDate=date(2023, 9, 28))
            gpu141 = Gpu(gpu_name="GeForce RTX 3090", manufacturer="MSI", gpu_brand="Nvidia", VRAM=16,
                         VRAM_type="GDDR5", msrp=1683, PCIe=3, ReleaseDate=date(2024, 3, 24))
            gpu142 = Gpu(gpu_name="GeForce RTX 2070 SuperUltra", manufacturer="EVGA", gpu_brand="Nvidia", VRAM=6,
                         VRAM_type="GDDR6X", msrp=1353, PCIe=5, ReleaseDate=date(2021, 2, 13))
            gpu143 = Gpu(gpu_name="GeForce RTX 3070Ultra", manufacturer="XFX", gpu_brand="Nvidia", VRAM=6,
                         VRAM_type="GDDR5", msrp=1089, PCIe=5, ReleaseDate=date(2022, 3, 16))
            gpu144 = Gpu(gpu_name="GeForce RTX 4070OC", manufacturer="EVGA", gpu_brand="Nvidia", VRAM=24,
                         VRAM_type="GDDR6", msrp=1197, PCIe=4, ReleaseDate=date(2021, 2, 24))
            gpu145 = Gpu(gpu_name="GeForce RTX 2080 TiX", manufacturer="XFX", gpu_brand="Nvidia", VRAM=16,
                         VRAM_type="GDDR6X", msrp=372, PCIe=5, ReleaseDate=date(2023, 10, 18))
            gpu146 = Gpu(gpu_name="GeForce RTX 4090Gaming", manufacturer="Gigabyte", gpu_brand="Nvidia", VRAM=10,
                         VRAM_type="GDDR6", msrp=1525, PCIe=5, ReleaseDate=date(2018, 4, 22))
            gpu147 = Gpu(gpu_name="GeForce RTX 2080 TiUltra", manufacturer="EVGA", gpu_brand="Nvidia", VRAM=16,
                         VRAM_type="GDDR6", msrp=1439, PCIe=5, ReleaseDate=date(2023, 3, 4))
            gpu148 = Gpu(gpu_name="ARC A750X", manufacturer="Zotac", gpu_brand="Intel", VRAM=8, VRAM_type="GDDR5X",
                         msrp=1167, PCIe=3, ReleaseDate=date(2020, 3, 11))
            gpu149 = Gpu(gpu_name="GeForce RTX 3080OC", manufacturer="XFX", gpu_brand="Nvidia", VRAM=16,
                         VRAM_type="GDDR6X", msrp=395, PCIe=3, ReleaseDate=date(2024, 11, 10))
            gpu150 = Gpu(gpu_name="Radeon RX 5700 XT", manufacturer="PowerColor", gpu_brand="AMD", VRAM=12,
                         VRAM_type="GDDR6X", msrp=433, PCIe=5, ReleaseDate=date(2023, 4, 19))
            gpu151 = Gpu(gpu_name="GeForce RTX 2070 Super", manufacturer="XFX", gpu_brand="Nvidia", VRAM=12,
                         VRAM_type="GDDR6", msrp=247, PCIe=5, ReleaseDate=date(2023, 11, 16))
            gpu152 = Gpu(gpu_name="GeForce RTX 2080 TiUltra", manufacturer="EVGA", gpu_brand="Nvidia", VRAM=6,
                         VRAM_type="GDDR6", msrp=784, PCIe=4, ReleaseDate=date(2021, 12, 28))
            gpu153 = Gpu(gpu_name="Radeon RX 6700 XT", manufacturer="XFX", gpu_brand="AMD", VRAM=24, VRAM_type="GDDR5X",
                         msrp=679, PCIe=4, ReleaseDate=date(2021, 11, 25))
            gpu154 = Gpu(gpu_name="Radeon RX 5700 XTX", manufacturer="Zotac", gpu_brand="AMD", VRAM=10,
                         VRAM_type="GDDR5", msrp=1419, PCIe=3, ReleaseDate=date(2020, 10, 7))
            gpu155 = Gpu(gpu_name="GeForce RTX 2080 TiOC", manufacturer="Sapphire", gpu_brand="Nvidia", VRAM=12,
                         VRAM_type="GDDR5X", msrp=811, PCIe=4, ReleaseDate=date(2023, 3, 17))
            gpu156 = Gpu(gpu_name="GeForce RTX 4090OC", manufacturer="Sapphire", gpu_brand="Nvidia", VRAM=24,
                         VRAM_type="GDDR6X", msrp=1069, PCIe=5, ReleaseDate=date(2022, 5, 19))
            gpu157 = Gpu(gpu_name="GeForce RTX 2080 TiX", manufacturer="PowerColor", gpu_brand="Nvidia", VRAM=6,
                         VRAM_type="GDDR6", msrp=628, PCIe=3, ReleaseDate=date(2023, 10, 9))
            gpu158 = Gpu(gpu_name="GeForce RTX 2080 TiUltra", manufacturer="PowerColor", gpu_brand="Nvidia", VRAM=16,
                         VRAM_type="GDDR5X", msrp=1602, PCIe=4, ReleaseDate=date(2023, 4, 14))
            gpu159 = Gpu(gpu_name="GeForce RTX 2070 Super", manufacturer="Gigabyte", gpu_brand="Nvidia", VRAM=12,
                         VRAM_type="GDDR5X", msrp=1565, PCIe=4, ReleaseDate=date(2019, 9, 15))
            gpu160 = Gpu(gpu_name="GeForce RTX 2080 TiUltra", manufacturer="Gigabyte", gpu_brand="Nvidia", VRAM=12,
                         VRAM_type="GDDR5", msrp=1439, PCIe=4, ReleaseDate=date(2023, 6, 26))
            gpu161 = Gpu(gpu_name="GeForce RTX 2080", manufacturer="Gigabyte", gpu_brand="Nvidia", VRAM=10,
                         VRAM_type="GDDR6X", msrp=989, PCIe=3, ReleaseDate=date(2018, 4, 6))
            gpu162 = Gpu(gpu_name="GeForce RTX 4070X", manufacturer="PowerColor", gpu_brand="Nvidia", VRAM=12,
                         VRAM_type="GDDR6", msrp=523, PCIe=5, ReleaseDate=date(2020, 6, 9))
            gpu163 = Gpu(gpu_name="GeForce RTX 3070X", manufacturer="PowerColor", gpu_brand="Nvidia", VRAM=12,
                         VRAM_type="GDDR5X", msrp=1301, PCIe=3, ReleaseDate=date(2022, 8, 5))
            gpu164 = Gpu(gpu_name="Radeon RX 6700 XTUltra", manufacturer="MSI", gpu_brand="AMD", VRAM=16,
                         VRAM_type="GDDR6", msrp=294, PCIe=5, ReleaseDate=date(2019, 3, 3))
            gpu165 = Gpu(gpu_name="GeForce RTX 2080X", manufacturer="Zotac", gpu_brand="Nvidia", VRAM=24,
                         VRAM_type="GDDR5X", msrp=664, PCIe=5, ReleaseDate=date(2024, 7, 13))
            gpu166 = Gpu(gpu_name="GeForce RTX 4070X", manufacturer="Gigabyte", gpu_brand="Nvidia", VRAM=24,
                         VRAM_type="GDDR6X", msrp=1567, PCIe=4, ReleaseDate=date(2024, 12, 4))
            gpu167 = Gpu(gpu_name="Radeon RX 6700 XTUltra", manufacturer="EVGA", gpu_brand="AMD", VRAM=10,
                         VRAM_type="GDDR5X", msrp=377, PCIe=4, ReleaseDate=date(2018, 8, 28))
            gpu168 = Gpu(gpu_name="Radeon RX 6700 XTGaming", manufacturer="Zotac", gpu_brand="AMD", VRAM=8,
                         VRAM_type="GDDR6X", msrp=1392, PCIe=3, ReleaseDate=date(2020, 9, 7))
            gpu169 = Gpu(gpu_name="GeForce RTX 3070Ultra", manufacturer="Sapphire", gpu_brand="Nvidia", VRAM=16,
                         VRAM_type="GDDR6X", msrp=1076, PCIe=5, ReleaseDate=date(2018, 5, 16))
            gpu170 = Gpu(gpu_name="GeForce RTX 3070", manufacturer="XFX", gpu_brand="Nvidia", VRAM=24,
                         VRAM_type="GDDR6X", msrp=990, PCIe=3, ReleaseDate=date(2019, 2, 24))
            gpu171 = Gpu(gpu_name="GeForce RTX 2080Ultra", manufacturer="Zotac", gpu_brand="Nvidia", VRAM=10,
                         VRAM_type="GDDR6", msrp=1473, PCIe=4, ReleaseDate=date(2024, 8, 22))
            gpu172 = Gpu(gpu_name="ARC A750", manufacturer="XFX", gpu_brand="Intel", VRAM=10, VRAM_type="GDDR5X",
                         msrp=456, PCIe=4, ReleaseDate=date(2019, 2, 11))
            gpu173 = Gpu(gpu_name="ARC A750OC", manufacturer="MSI", gpu_brand="Intel", VRAM=24, VRAM_type="GDDR5X",
                         msrp=311, PCIe=3, ReleaseDate=date(2024, 11, 24))
            gpu174 = Gpu(gpu_name="GeForce RTX 2070 SuperUltra", manufacturer="XFX", gpu_brand="Nvidia", VRAM=16,
                         VRAM_type="GDDR6X", msrp=245, PCIe=4, ReleaseDate=date(2018, 12, 2))
            gpu175 = Gpu(gpu_name="Radeon RX 5700 XTOC", manufacturer="ASUS", gpu_brand="AMD", VRAM=8,
                         VRAM_type="GDDR5", msrp=1392, PCIe=4, ReleaseDate=date(2018, 2, 28))
            gpu176 = Gpu(gpu_name="GeForce RTX 3090OC", manufacturer="Zotac", gpu_brand="Nvidia", VRAM=6,
                         VRAM_type="GDDR5X", msrp=739, PCIe=3, ReleaseDate=date(2020, 1, 27))
            gpu177 = Gpu(gpu_name="GeForce RTX 2080 TiOC", manufacturer="Sapphire", gpu_brand="Nvidia", VRAM=10,
                         VRAM_type="GDDR6", msrp=689, PCIe=5, ReleaseDate=date(2023, 6, 4))
            gpu178 = Gpu(gpu_name="GeForce RTX 3070X", manufacturer="Zotac", gpu_brand="Nvidia", VRAM=16,
                         VRAM_type="GDDR5X", msrp=1249, PCIe=3, ReleaseDate=date(2024, 4, 9))
            gpu179 = Gpu(gpu_name="GeForce RTX 3090OC", manufacturer="Zotac", gpu_brand="Nvidia", VRAM=16,
                         VRAM_type="GDDR6", msrp=1589, PCIe=4, ReleaseDate=date(2024, 3, 25))
            gpu180 = Gpu(gpu_name="GeForce RTX 4090Ultra", manufacturer="Sapphire", gpu_brand="Nvidia", VRAM=10,
                         VRAM_type="GDDR5X", msrp=1683, PCIe=5, ReleaseDate=date(2023, 8, 5))
            gpu181 = Gpu(gpu_name="GeForce RTX 4090Gaming", manufacturer="Gigabyte", gpu_brand="Nvidia", VRAM=6,
                         VRAM_type="GDDR5", msrp=723, PCIe=4, ReleaseDate=date(2023, 7, 16))
            gpu182 = Gpu(gpu_name="GeForce RTX 4090Gaming", manufacturer="Sapphire", gpu_brand="Nvidia", VRAM=8,
                         VRAM_type="GDDR5", msrp=697, PCIe=3, ReleaseDate=date(2019, 10, 3))
            gpu183 = Gpu(gpu_name="GeForce RTX 2080OC", manufacturer="MSI", gpu_brand="Nvidia", VRAM=6,
                         VRAM_type="GDDR6", msrp=1027, PCIe=3, ReleaseDate=date(2023, 2, 14))
            gpu184 = Gpu(gpu_name="ARC A750Gaming", manufacturer="Gigabyte", gpu_brand="Intel", VRAM=8,
                         VRAM_type="GDDR6X", msrp=1738, PCIe=5, ReleaseDate=date(2024, 11, 14))
            gpu185 = Gpu(gpu_name="GeForce RTX 3080OC", manufacturer="PowerColor", gpu_brand="Nvidia", VRAM=6,
                         VRAM_type="GDDR5", msrp=244, PCIe=5, ReleaseDate=date(2022, 2, 19))
            gpu186 = Gpu(gpu_name="GeForce RTX 3090X", manufacturer="PowerColor", gpu_brand="Nvidia", VRAM=10,
                         VRAM_type="GDDR6", msrp=1071, PCIe=3, ReleaseDate=date(2020, 10, 7))
            gpu187 = Gpu(gpu_name="Radeon RX 6800Gaming", manufacturer="MSI", gpu_brand="AMD", VRAM=10,
                         VRAM_type="GDDR6", msrp=1434, PCIe=4, ReleaseDate=date(2019, 3, 21))
            gpu188 = Gpu(gpu_name="GeForce RTX 4090Gaming", manufacturer="XFX", gpu_brand="Nvidia", VRAM=8,
                         VRAM_type="GDDR5", msrp=1027, PCIe=5, ReleaseDate=date(2023, 3, 4))
            gpu189 = Gpu(gpu_name="GeForce RTX 2070 Super", manufacturer="Sapphire", gpu_brand="Nvidia", VRAM=12,
                         VRAM_type="GDDR6", msrp=345, PCIe=3, ReleaseDate=date(2023, 7, 17))
            gpu190 = Gpu(gpu_name="GeForce RTX 2080Ultra", manufacturer="XFX", gpu_brand="Nvidia", VRAM=8,
                         VRAM_type="GDDR6X", msrp=680, PCIe=5, ReleaseDate=date(2022, 1, 19))
            gpu191 = Gpu(gpu_name="GeForce RTX 4090OC", manufacturer="ASUS", gpu_brand="Nvidia", VRAM=16,
                         VRAM_type="GDDR5", msrp=787, PCIe=3, ReleaseDate=date(2023, 5, 28))
            gpu192 = Gpu(gpu_name="ARC A750Gaming", manufacturer="PowerColor", gpu_brand="Intel", VRAM=6,
                         VRAM_type="GDDR5X", msrp=897, PCIe=4, ReleaseDate=date(2023, 2, 15))
            gpu193 = Gpu(gpu_name="GeForce RTX 2070 SuperGaming", manufacturer="Gigabyte", gpu_brand="Nvidia", VRAM=8,
                         VRAM_type="GDDR6X", msrp=1515, PCIe=3, ReleaseDate=date(2019, 1, 8))
            gpu194 = Gpu(gpu_name="Radeon RX 7900 XTX", manufacturer="ASUS", gpu_brand="AMD", VRAM=16,
                         VRAM_type="GDDR6", msrp=393, PCIe=3, ReleaseDate=date(2024, 2, 15))
            gpu195 = Gpu(gpu_name="Radeon RX 6800X", manufacturer="MSI", gpu_brand="AMD", VRAM=16, VRAM_type="GDDR6",
                         msrp=1400, PCIe=4, ReleaseDate=date(2021, 1, 13))
            gpu196 = Gpu(gpu_name="GeForce RTX 4090Ultra", manufacturer="XFX", gpu_brand="Nvidia", VRAM=16,
                         VRAM_type="GDDR5X", msrp=610, PCIe=4, ReleaseDate=date(2023, 3, 25))
            gpu197 = Gpu(gpu_name="GeForce RTX 4090OC", manufacturer="Zotac", gpu_brand="Nvidia", VRAM=12,
                         VRAM_type="GDDR6", msrp=1091, PCIe=3, ReleaseDate=date(2023, 12, 1))
            gpu198 = Gpu(gpu_name="Radeon RX 7900 XTXX", manufacturer="ASUS", gpu_brand="AMD", VRAM=6,
                         VRAM_type="GDDR6", msrp=1327, PCIe=4, ReleaseDate=date(2020, 3, 14))
            gpu199 = Gpu(gpu_name="Radeon RX 6800", manufacturer="ASUS", gpu_brand="AMD", VRAM=16, VRAM_type="GDDR5X",
                         msrp=789, PCIe=4, ReleaseDate=date(2019, 6, 16))
            gpu200 = Gpu(gpu_name="Radeon RX 5700 XT", manufacturer="XFX", gpu_brand="AMD", VRAM=12, VRAM_type="GDDR5",
                         msrp=515, PCIe=4, ReleaseDate=date(2022, 1, 17))
            gpu201 = Gpu(gpu_name="Radeon RX 6800Gaming", manufacturer="MSI", gpu_brand="AMD", VRAM=8,
                         VRAM_type="GDDR5", msrp=315, PCIe=3, ReleaseDate=date(2020, 11, 4))
            gpu202 = Gpu(gpu_name="GeForce RTX 3070", manufacturer="ASUS", gpu_brand="Nvidia", VRAM=6,
                         VRAM_type="GDDR5", msrp=1195, PCIe=5, ReleaseDate=date(2024, 9, 13))
            gpu203 = Gpu(gpu_name="ARC A750", manufacturer="EVGA", gpu_brand="Intel", VRAM=6, VRAM_type="GDDR5X",
                         msrp=766, PCIe=3, ReleaseDate=date(2023, 10, 10))
            gpu204 = Gpu(gpu_name="GeForce RTX 4090Ultra", manufacturer="PowerColor", gpu_brand="Nvidia", VRAM=12,
                         VRAM_type="GDDR5X", msrp=459, PCIe=4, ReleaseDate=date(2024, 5, 14))
            gpu205 = Gpu(gpu_name="Radeon RX 7900 XTXX", manufacturer="Zotac", gpu_brand="AMD", VRAM=6,
                         VRAM_type="GDDR6X", msrp=1341, PCIe=4, ReleaseDate=date(2019, 6, 3))
            gpu206 = Gpu(gpu_name="Radeon RX 7900 XTX", manufacturer="ASUS", gpu_brand="AMD", VRAM=6,
                         VRAM_type="GDDR6X", msrp=1138, PCIe=3, ReleaseDate=date(2019, 4, 9))
            gpu207 = Gpu(gpu_name="GeForce RTX 3070OC", manufacturer="Zotac", gpu_brand="Nvidia", VRAM=24,
                         VRAM_type="GDDR5", msrp=1593, PCIe=3, ReleaseDate=date(2019, 5, 19))
            gpu208 = Gpu(gpu_name="GeForce RTX 3090OC", manufacturer="Gigabyte", gpu_brand="Nvidia", VRAM=6,
                         VRAM_type="GDDR5", msrp=1054, PCIe=3, ReleaseDate=date(2022, 12, 20))
            gpu209 = Gpu(gpu_name="GeForce RTX 2080", manufacturer="ASUS", gpu_brand="Nvidia", VRAM=10,
                         VRAM_type="GDDR5", msrp=1441, PCIe=3, ReleaseDate=date(2024, 1, 11))
            gpu210 = Gpu(gpu_name="Radeon RX 6700 XTUltra", manufacturer="Zotac", gpu_brand="AMD", VRAM=16,
                         VRAM_type="GDDR5X", msrp=1258, PCIe=4, ReleaseDate=date(2018, 7, 23))
            gpu211 = Gpu(gpu_name="Radeon RX 6800OC", manufacturer="PowerColor", gpu_brand="AMD", VRAM=6,
                         VRAM_type="GDDR6X", msrp=211, PCIe=3, ReleaseDate=date(2020, 11, 2))
            gpu212 = Gpu(gpu_name="GeForce RTX 4090X", manufacturer="Zotac", gpu_brand="Nvidia", VRAM=16,
                         VRAM_type="GDDR5X", msrp=325, PCIe=3, ReleaseDate=date(2024, 2, 7))
            gpu213 = Gpu(gpu_name="GeForce RTX 2080 Ti", manufacturer="PowerColor", gpu_brand="Nvidia", VRAM=12,
                         VRAM_type="GDDR6X", msrp=1427, PCIe=3, ReleaseDate=date(2020, 2, 4))
            gpu214 = Gpu(gpu_name="Radeon RX 6800OC", manufacturer="MSI", gpu_brand="AMD", VRAM=10, VRAM_type="GDDR5X",
                         msrp=1706, PCIe=3, ReleaseDate=date(2023, 5, 1))
            gpu215 = Gpu(gpu_name="GeForce RTX 2070 SuperX", manufacturer="EVGA", gpu_brand="Nvidia", VRAM=8,
                         VRAM_type="GDDR5", msrp=1202, PCIe=4, ReleaseDate=date(2021, 4, 14))
            gpu216 = Gpu(gpu_name="GeForce RTX 2080Gaming", manufacturer="PowerColor", gpu_brand="Nvidia", VRAM=12,
                         VRAM_type="GDDR6", msrp=1185, PCIe=4, ReleaseDate=date(2023, 5, 16))
            gpu217 = Gpu(gpu_name="GeForce RTX 2080 TiUltra", manufacturer="EVGA", gpu_brand="Nvidia", VRAM=24,
                         VRAM_type="GDDR6", msrp=1593, PCIe=3, ReleaseDate=date(2024, 12, 7))
            gpu218 = Gpu(gpu_name="GeForce RTX 4090Ultra", manufacturer="EVGA", gpu_brand="Nvidia", VRAM=24,
                         VRAM_type="GDDR6", msrp=1675, PCIe=4, ReleaseDate=date(2020, 1, 3))
            gpu219 = Gpu(gpu_name="GeForce RTX 2080 Ti", manufacturer="Gigabyte", gpu_brand="Nvidia", VRAM=6,
                         VRAM_type="GDDR5X", msrp=1358, PCIe=3, ReleaseDate=date(2020, 1, 5))
            gpu220 = Gpu(gpu_name="GeForce RTX 4090Gaming", manufacturer="Gigabyte", gpu_brand="Nvidia", VRAM=6,
                         VRAM_type="GDDR5X", msrp=1311, PCIe=4, ReleaseDate=date(2019, 5, 15))
            gpu221 = Gpu(gpu_name="Radeon RX 7900 XTXOC", manufacturer="PowerColor", gpu_brand="AMD", VRAM=24,
                         VRAM_type="GDDR5", msrp=1163, PCIe=4, ReleaseDate=date(2019, 8, 16))
            gpu222 = Gpu(gpu_name="GeForce RTX 2080 TiGaming", manufacturer="PowerColor", gpu_brand="Nvidia", VRAM=6,
                         VRAM_type="GDDR5", msrp=683, PCIe=4, ReleaseDate=date(2021, 10, 20))
            gpu223 = Gpu(gpu_name="GeForce RTX 2070 SuperOC", manufacturer="Sapphire", gpu_brand="Nvidia", VRAM=10,
                         VRAM_type="GDDR6X", msrp=1626, PCIe=4, ReleaseDate=date(2023, 4, 25))
            gpu224 = Gpu(gpu_name="GeForce RTX 2070 Super", manufacturer="Zotac", gpu_brand="Nvidia", VRAM=8,
                         VRAM_type="GDDR6X", msrp=1692, PCIe=4, ReleaseDate=date(2023, 9, 13))
            gpu225 = Gpu(gpu_name="GeForce RTX 3090Ultra", manufacturer="MSI", gpu_brand="Nvidia", VRAM=12,
                         VRAM_type="GDDR5", msrp=226, PCIe=3, ReleaseDate=date(2024, 7, 6))
            gpu226 = Gpu(gpu_name="GeForce RTX 3070OC", manufacturer="Zotac", gpu_brand="Nvidia", VRAM=24,
                         VRAM_type="GDDR6", msrp=1124, PCIe=3, ReleaseDate=date(2018, 9, 17))
            gpu227 = Gpu(gpu_name="GeForce RTX 2070 SuperGaming", manufacturer="Zotac", gpu_brand="Nvidia", VRAM=6,
                         VRAM_type="GDDR6", msrp=202, PCIe=3, ReleaseDate=date(2023, 10, 23))
            gpu228 = Gpu(gpu_name="Radeon RX 6700 XTOC", manufacturer="Zotac", gpu_brand="AMD", VRAM=10,
                         VRAM_type="GDDR6X", msrp=1466, PCIe=4, ReleaseDate=date(2024, 8, 8))
            gpu229 = Gpu(gpu_name="ARC A750Ultra", manufacturer="Zotac", gpu_brand="Intel", VRAM=8, VRAM_type="GDDR5",
                         msrp=467, PCIe=5, ReleaseDate=date(2020, 6, 20))
            gpu230 = Gpu(gpu_name="GeForce RTX 3070OC", manufacturer="XFX", gpu_brand="Nvidia", VRAM=8,
                         VRAM_type="GDDR5", msrp=1215, PCIe=5, ReleaseDate=date(2021, 10, 9))
            gpu231 = Gpu(gpu_name="GeForce RTX 2080OC", manufacturer="XFX", gpu_brand="Nvidia", VRAM=8,
                         VRAM_type="GDDR6X", msrp=797, PCIe=4, ReleaseDate=date(2021, 3, 23))
            gpu232 = Gpu(gpu_name="Radeon RX 7900 XTX", manufacturer="Gigabyte", gpu_brand="AMD", VRAM=8,
                         VRAM_type="GDDR6", msrp=829, PCIe=3, ReleaseDate=date(2024, 12, 9))
            gpu233 = Gpu(gpu_name="ARC A770Ultra", manufacturer="MSI", gpu_brand="Intel", VRAM=16, VRAM_type="GDDR5X",
                         msrp=1367, PCIe=5, ReleaseDate=date(2019, 11, 4))
            gpu234 = Gpu(gpu_name="GeForce RTX 3090X", manufacturer="EVGA", gpu_brand="Nvidia", VRAM=8,
                         VRAM_type="GDDR5", msrp=1347, PCIe=4, ReleaseDate=date(2022, 7, 10))
            gpu235 = Gpu(gpu_name="Radeon RX 6700 XTOC", manufacturer="XFX", gpu_brand="AMD", VRAM=12,
                         VRAM_type="GDDR5", msrp=644, PCIe=5, ReleaseDate=date(2023, 3, 25))
            gpu236 = Gpu(gpu_name="ARC A750X", manufacturer="MSI", gpu_brand="Intel", VRAM=8, VRAM_type="GDDR6X",
                         msrp=1385, PCIe=3, ReleaseDate=date(2020, 12, 13))
            gpu237 = Gpu(gpu_name="GeForce RTX 4070Gaming", manufacturer="ASUS", gpu_brand="Nvidia", VRAM=8,
                         VRAM_type="GDDR5", msrp=1136, PCIe=4, ReleaseDate=date(2020, 11, 26))
            gpu238 = Gpu(gpu_name="GeForce RTX 4070Ultra", manufacturer="ASUS", gpu_brand="Nvidia", VRAM=12,
                         VRAM_type="GDDR6", msrp=1182, PCIe=4, ReleaseDate=date(2024, 10, 28))
            gpu239 = Gpu(gpu_name="GeForce RTX 3080Gaming", manufacturer="Sapphire", gpu_brand="Nvidia", VRAM=10,
                         VRAM_type="GDDR6", msrp=292, PCIe=3, ReleaseDate=date(2020, 6, 25))
            gpu240 = Gpu(gpu_name="Radeon RX 7900 XTXGaming", manufacturer="ASUS", gpu_brand="AMD", VRAM=24,
                         VRAM_type="GDDR5X", msrp=1595, PCIe=5, ReleaseDate=date(2022, 2, 2))
            gpu241 = Gpu(gpu_name="GeForce RTX 3070Ultra", manufacturer="ASUS", gpu_brand="Nvidia", VRAM=24,
                         VRAM_type="GDDR6X", msrp=759, PCIe=4, ReleaseDate=date(2019, 11, 18))
            gpu242 = Gpu(gpu_name="GeForce RTX 4090Gaming", manufacturer="Zotac", gpu_brand="Nvidia", VRAM=8,
                         VRAM_type="GDDR5", msrp=759, PCIe=5, ReleaseDate=date(2019, 7, 20))
            gpu243 = Gpu(gpu_name="GeForce RTX 3090X", manufacturer="Zotac", gpu_brand="Nvidia", VRAM=16,
                         VRAM_type="GDDR5X", msrp=637, PCIe=5, ReleaseDate=date(2023, 8, 19))
            gpu244 = Gpu(gpu_name="GeForce RTX 2080X", manufacturer="XFX", gpu_brand="Nvidia", VRAM=12,
                         VRAM_type="GDDR5", msrp=1574, PCIe=4, ReleaseDate=date(2021, 2, 5))
            gpu245 = Gpu(gpu_name="Radeon RX 5700 XTGaming", manufacturer="ASUS", gpu_brand="AMD", VRAM=10,
                         VRAM_type="GDDR6X", msrp=1652, PCIe=5, ReleaseDate=date(2024, 11, 5))
            gpu246 = Gpu(gpu_name="ARC A770OC", manufacturer="ASUS", gpu_brand="Intel", VRAM=16, VRAM_type="GDDR5X",
                         msrp=1234, PCIe=4, ReleaseDate=date(2020, 11, 16))
            gpu247 = Gpu(gpu_name="Radeon RX 7900 XTXGaming", manufacturer="Sapphire", gpu_brand="AMD", VRAM=6,
                         VRAM_type="GDDR6X", msrp=1523, PCIe=4, ReleaseDate=date(2019, 2, 5))
            gpu248 = Gpu(gpu_name="GeForce RTX 4070", manufacturer="MSI", gpu_brand="Nvidia", VRAM=24,
                         VRAM_type="GDDR6", msrp=1500, PCIe=5, ReleaseDate=date(2019, 7, 23))
            gpu249 = Gpu(gpu_name="GeForce RTX 2070 SuperOC", manufacturer="ASUS", gpu_brand="Nvidia", VRAM=8,
                         VRAM_type="GDDR5", msrp=1178, PCIe=5, ReleaseDate=date(2020, 7, 25))
            gpu250 = Gpu(gpu_name="GeForce RTX 2070 SuperOC", manufacturer="XFX", gpu_brand="Nvidia", VRAM=24,
                         VRAM_type="GDDR6X", msrp=1757, PCIe=5, ReleaseDate=date(2018, 8, 1))
            gpu251 = Gpu(gpu_name="GeForce RTX 3090Gaming", manufacturer="XFX", gpu_brand="Nvidia", VRAM=16,
                         VRAM_type="GDDR5X", msrp=1712, PCIe=5, ReleaseDate=date(2022, 9, 17))
            gpu252 = Gpu(gpu_name="Radeon RX 6800OC", manufacturer="MSI", gpu_brand="AMD", VRAM=6, VRAM_type="GDDR6X",
                         msrp=1383, PCIe=4, ReleaseDate=date(2020, 7, 22))
            gpu253 = Gpu(gpu_name="GeForce RTX 3080X", manufacturer="ASUS", gpu_brand="Nvidia", VRAM=10,
                         VRAM_type="GDDR6X", msrp=999, PCIe=3, ReleaseDate=date(2023, 5, 15))
            gpu254 = Gpu(gpu_name="GeForce RTX 3080X", manufacturer="MSI", gpu_brand="Nvidia", VRAM=12,
                         VRAM_type="GDDR5", msrp=422, PCIe=5, ReleaseDate=date(2023, 10, 10))
            gpu255 = Gpu(gpu_name="GeForce RTX 4090OC", manufacturer="PowerColor", gpu_brand="Nvidia", VRAM=12,
                         VRAM_type="GDDR6X", msrp=802, PCIe=5, ReleaseDate=date(2024, 12, 15))
            gpu256 = Gpu(gpu_name="GeForce RTX 2080Ultra", manufacturer="Sapphire", gpu_brand="Nvidia", VRAM=12,
                         VRAM_type="GDDR6X", msrp=1789, PCIe=4, ReleaseDate=date(2021, 1, 25))
            gpu257 = Gpu(gpu_name="GeForce RTX 2070 SuperX", manufacturer="Gigabyte", gpu_brand="Nvidia", VRAM=10,
                         VRAM_type="GDDR5", msrp=471, PCIe=5, ReleaseDate=date(2018, 6, 22))
            gpu258 = Gpu(gpu_name="GeForce RTX 2080 TiGaming", manufacturer="MSI", gpu_brand="Nvidia", VRAM=10,
                         VRAM_type="GDDR5", msrp=1599, PCIe=4, ReleaseDate=date(2020, 3, 8))
            gpu259 = Gpu(gpu_name="GeForce RTX 2070 Super", manufacturer="MSI", gpu_brand="Nvidia", VRAM=8,
                         VRAM_type="GDDR6X", msrp=1385, PCIe=5, ReleaseDate=date(2018, 8, 19))
            gpu260 = Gpu(gpu_name="Radeon RX 5700 XTOC", manufacturer="XFX", gpu_brand="AMD", VRAM=10,
                         VRAM_type="GDDR5", msrp=1460, PCIe=5, ReleaseDate=date(2024, 6, 28))
            gpu261 = Gpu(gpu_name="ARC A750", manufacturer="ASUS", gpu_brand="Intel", VRAM=10, VRAM_type="GDDR5X",
                         msrp=1796, PCIe=3, ReleaseDate=date(2022, 2, 21))
            gpu262 = Gpu(gpu_name="GeForce RTX 3090Ultra", manufacturer="PowerColor", gpu_brand="Nvidia", VRAM=10,
                         VRAM_type="GDDR5X", msrp=346, PCIe=4, ReleaseDate=date(2021, 6, 5))
            gpu263 = Gpu(gpu_name="Radeon RX 5700 XTOC", manufacturer="PowerColor", gpu_brand="AMD", VRAM=16,
                         VRAM_type="GDDR5X", msrp=1226, PCIe=4, ReleaseDate=date(2023, 5, 24))
            gpu264 = Gpu(gpu_name="GeForce RTX 3080Gaming", manufacturer="Zotac", gpu_brand="Nvidia", VRAM=24,
                         VRAM_type="GDDR6X", msrp=1572, PCIe=3, ReleaseDate=date(2018, 6, 15))
            gpu265 = Gpu(gpu_name="GeForce RTX 3080Ultra", manufacturer="Zotac", gpu_brand="Nvidia", VRAM=12,
                         VRAM_type="GDDR5", msrp=1497, PCIe=5, ReleaseDate=date(2020, 11, 15))
            gpu266 = Gpu(gpu_name="GeForce RTX 2070 SuperGaming", manufacturer="Zotac", gpu_brand="Nvidia", VRAM=6,
                         VRAM_type="GDDR6", msrp=756, PCIe=3, ReleaseDate=date(2024, 11, 13))
            gpu267 = Gpu(gpu_name="Radeon RX 7900 XTX", manufacturer="XFX", gpu_brand="AMD", VRAM=12, VRAM_type="GDDR6",
                         msrp=329, PCIe=3, ReleaseDate=date(2023, 7, 22))
            gpu268 = Gpu(gpu_name="Radeon RX 5700 XTUltra", manufacturer="XFX", gpu_brand="AMD", VRAM=24,
                         VRAM_type="GDDR6X", msrp=584, PCIe=5, ReleaseDate=date(2020, 5, 1))
            gpu269 = Gpu(gpu_name="Radeon RX 6700 XTGaming", manufacturer="XFX", gpu_brand="AMD", VRAM=6,
                         VRAM_type="GDDR6", msrp=551, PCIe=4, ReleaseDate=date(2018, 12, 3))
            gpu270 = Gpu(gpu_name="Radeon RX 6700 XTOC", manufacturer="XFX", gpu_brand="AMD", VRAM=8, VRAM_type="GDDR6",
                         msrp=375, PCIe=3, ReleaseDate=date(2024, 7, 17))
            gpu271 = Gpu(gpu_name="Radeon RX 6700 XTUltra", manufacturer="Gigabyte", gpu_brand="AMD", VRAM=16,
                         VRAM_type="GDDR6X", msrp=621, PCIe=3, ReleaseDate=date(2022, 10, 24))
            gpu272 = Gpu(gpu_name="Radeon RX 6800OC", manufacturer="Gigabyte", gpu_brand="AMD", VRAM=6,
                         VRAM_type="GDDR5", msrp=1406, PCIe=5, ReleaseDate=date(2022, 4, 6))
            gpu273 = Gpu(gpu_name="GeForce RTX 4090", manufacturer="MSI", gpu_brand="Nvidia", VRAM=12,
                         VRAM_type="GDDR5X", msrp=848, PCIe=3, ReleaseDate=date(2024, 5, 18))
            gpu274 = Gpu(gpu_name="GeForce RTX 3090OC", manufacturer="Gigabyte", gpu_brand="Nvidia", VRAM=16,
                         VRAM_type="GDDR5", msrp=1161, PCIe=3, ReleaseDate=date(2019, 11, 12))
            gpu275 = Gpu(gpu_name="Radeon RX 5700 XT", manufacturer="Zotac", gpu_brand="AMD", VRAM=24,
                         VRAM_type="GDDR5", msrp=855, PCIe=4, ReleaseDate=date(2021, 7, 23))
            gpu276 = Gpu(gpu_name="GeForce RTX 3070", manufacturer="ASUS", gpu_brand="Nvidia", VRAM=24,
                         VRAM_type="GDDR6", msrp=556, PCIe=4, ReleaseDate=date(2024, 8, 6))
            gpu277 = Gpu(gpu_name="Radeon RX 7900 XTXUltra", manufacturer="Gigabyte", gpu_brand="AMD", VRAM=24,
                         VRAM_type="GDDR5", msrp=1530, PCIe=5, ReleaseDate=date(2023, 12, 13))
            gpu278 = Gpu(gpu_name="GeForce RTX 2070 SuperGaming", manufacturer="ASUS", gpu_brand="Nvidia", VRAM=12,
                         VRAM_type="GDDR5", msrp=1637, PCIe=5, ReleaseDate=date(2023, 2, 24))
            gpu279 = Gpu(gpu_name="Radeon RX 7900 XTX", manufacturer="Gigabyte", gpu_brand="AMD", VRAM=8,
                         VRAM_type="GDDR6X", msrp=768, PCIe=4, ReleaseDate=date(2023, 2, 6))
            gpu280 = Gpu(gpu_name="GeForce RTX 2080 TiX", manufacturer="PowerColor", gpu_brand="Nvidia", VRAM=24,
                         VRAM_type="GDDR5X", msrp=1296, PCIe=4, ReleaseDate=date(2020, 3, 6))
            gpu281 = Gpu(gpu_name="GeForce RTX 2070 Super", manufacturer="Gigabyte", gpu_brand="Nvidia", VRAM=8,
                         VRAM_type="GDDR5X", msrp=783, PCIe=3, ReleaseDate=date(2024, 7, 18))
            gpu282 = Gpu(gpu_name="Radeon RX 7900 XTXGaming", manufacturer="Zotac", gpu_brand="AMD", VRAM=10,
                         VRAM_type="GDDR5", msrp=204, PCIe=3, ReleaseDate=date(2021, 10, 16))
            gpu283 = Gpu(gpu_name="Radeon RX 6700 XTX", manufacturer="MSI", gpu_brand="AMD", VRAM=10, VRAM_type="GDDR6",
                         msrp=1389, PCIe=4, ReleaseDate=date(2023, 1, 10))
            gpu284 = Gpu(gpu_name="ARC A770Ultra", manufacturer="Sapphire", gpu_brand="Intel", VRAM=6,
                         VRAM_type="GDDR6", msrp=1798, PCIe=3, ReleaseDate=date(2021, 4, 4))
            gpu285 = Gpu(gpu_name="GeForce RTX 2080 TiGaming", manufacturer="XFX", gpu_brand="Nvidia", VRAM=24,
                         VRAM_type="GDDR6", msrp=729, PCIe=3, ReleaseDate=date(2022, 2, 22))
            gpu286 = Gpu(gpu_name="GeForce RTX 3090", manufacturer="MSI", gpu_brand="Nvidia", VRAM=16,
                         VRAM_type="GDDR5X", msrp=570, PCIe=3, ReleaseDate=date(2018, 7, 22))
            gpu287 = Gpu(gpu_name="GeForce RTX 4090Ultra", manufacturer="ASUS", gpu_brand="Nvidia", VRAM=8,
                         VRAM_type="GDDR6", msrp=1788, PCIe=3, ReleaseDate=date(2018, 1, 3))
            gpu288 = Gpu(gpu_name="GeForce RTX 2080 TiOC", manufacturer="EVGA", gpu_brand="Nvidia", VRAM=12,
                         VRAM_type="GDDR6", msrp=619, PCIe=4, ReleaseDate=date(2024, 4, 18))
            gpu289 = Gpu(gpu_name="GeForce RTX 3090Gaming", manufacturer="XFX", gpu_brand="Nvidia", VRAM=24,
                         VRAM_type="GDDR5", msrp=1608, PCIe=5, ReleaseDate=date(2023, 9, 14))
            gpu290 = Gpu(gpu_name="ARC A770", manufacturer="Gigabyte", gpu_brand="Intel", VRAM=24, VRAM_type="GDDR5X",
                         msrp=200, PCIe=4, ReleaseDate=date(2024, 4, 17))
            gpu291 = Gpu(gpu_name="GeForce RTX 3090", manufacturer="Sapphire", gpu_brand="Nvidia", VRAM=24,
                         VRAM_type="GDDR6X", msrp=1171, PCIe=3, ReleaseDate=date(2023, 9, 24))
            gpu292 = Gpu(gpu_name="GeForce RTX 3090OC", manufacturer="Zotac", gpu_brand="Nvidia", VRAM=8,
                         VRAM_type="GDDR6", msrp=1762, PCIe=4, ReleaseDate=date(2021, 12, 19))
            gpu293 = Gpu(gpu_name="GeForce RTX 2080 Ti", manufacturer="ASUS", gpu_brand="Nvidia", VRAM=24,
                         VRAM_type="GDDR5X", msrp=1784, PCIe=4, ReleaseDate=date(2021, 4, 12))
            gpu294 = Gpu(gpu_name="Radeon RX 5700 XT", manufacturer="Zotac", gpu_brand="AMD", VRAM=8,
                         VRAM_type="GDDR5X", msrp=1089, PCIe=4, ReleaseDate=date(2024, 9, 18))
            gpu295 = Gpu(gpu_name="Radeon RX 5700 XTGaming", manufacturer="MSI", gpu_brand="AMD", VRAM=16,
                         VRAM_type="GDDR6", msrp=201, PCIe=3, ReleaseDate=date(2022, 2, 9))
            gpu296 = Gpu(gpu_name="GeForce RTX 4090", manufacturer="XFX", gpu_brand="Nvidia", VRAM=16,
                         VRAM_type="GDDR5", msrp=816, PCIe=4, ReleaseDate=date(2019, 6, 27))
            gpu297 = Gpu(gpu_name="Radeon RX 5700 XTOC", manufacturer="MSI", gpu_brand="AMD", VRAM=8,
                         VRAM_type="GDDR5X", msrp=1122, PCIe=5, ReleaseDate=date(2022, 1, 15))
            gpu298 = Gpu(gpu_name="ARC A770Ultra", manufacturer="Zotac", gpu_brand="Intel", VRAM=10, VRAM_type="GDDR5X",
                         msrp=995, PCIe=4, ReleaseDate=date(2022, 11, 25))
            gpu299 = Gpu(gpu_name="GeForce RTX 3090Ultra", manufacturer="MSI", gpu_brand="Nvidia", VRAM=24,
                         VRAM_type="GDDR5", msrp=991, PCIe=5, ReleaseDate=date(2020, 4, 12))
            gpu300 = Gpu(gpu_name="GeForce RTX 3090Gaming", manufacturer="ASUS", gpu_brand="Nvidia", VRAM=6,
                         VRAM_type="GDDR6", msrp=403, PCIe=4, ReleaseDate=date(2024, 5, 23))

            db.session.add_all(
                [gpu1, gpu2, gpu3, gpu4, gpu5, gpu6, gpu7, gpu8, gpu9, gpu10, gpu11, gpu12, gpu13, gpu14, gpu15, gpu16,
                 gpu17, gpu18, gpu19, gpu20, gpu21, gpu22, gpu23, gpu24, gpu25, gpu26, gpu27, gpu28, gpu29, gpu30,
                 gpu31, gpu32, gpu33, gpu34, gpu35, gpu36, gpu37, gpu38, gpu39, gpu40, gpu41, gpu42, gpu43, gpu44,
                 gpu45, gpu46, gpu47, gpu48, gpu49, gpu50, gpu51, gpu52, gpu53, gpu54, gpu55, gpu56, gpu57, gpu58,
                 gpu59, gpu60, gpu61, gpu62, gpu63, gpu64, gpu65, gpu66, gpu67, gpu68, gpu69, gpu70, gpu71, gpu72,
                 gpu73, gpu74, gpu75, gpu76, gpu77, gpu78, gpu79, gpu80, gpu81, gpu82, gpu83, gpu84, gpu85, gpu86,
                 gpu87, gpu88, gpu89, gpu90, gpu91, gpu92, gpu93, gpu94, gpu95, gpu96, gpu97, gpu98, gpu99, gpu100,
                 gpu101, gpu102, gpu103, gpu104, gpu105, gpu106, gpu107, gpu108, gpu109, gpu110, gpu111, gpu112, gpu113,
                 gpu114, gpu115, gpu116, gpu117, gpu118, gpu119, gpu120, gpu121, gpu122, gpu123, gpu124, gpu125, gpu126,
                 gpu127, gpu128, gpu129, gpu130, gpu131, gpu132, gpu133, gpu134, gpu135, gpu136, gpu137, gpu138, gpu139,
                 gpu140, gpu141, gpu142, gpu143, gpu144, gpu145, gpu146, gpu147, gpu148, gpu149, gpu150, gpu151, gpu152,
                 gpu153, gpu154, gpu155, gpu156, gpu157, gpu158, gpu159, gpu160, gpu161, gpu162, gpu163, gpu164, gpu165,
                 gpu166, gpu167, gpu168, gpu169, gpu170, gpu171, gpu172, gpu173, gpu174, gpu175, gpu176, gpu177, gpu178,
                 gpu179, gpu180, gpu181, gpu182, gpu183, gpu184, gpu185, gpu186, gpu187, gpu188, gpu189, gpu190, gpu191,
                 gpu192, gpu193, gpu194, gpu195, gpu196, gpu197, gpu198, gpu199, gpu200, gpu201, gpu202, gpu203, gpu204,
                 gpu205, gpu206, gpu207, gpu208, gpu209, gpu210, gpu211, gpu212, gpu213, gpu214, gpu215, gpu216, gpu217,
                 gpu218, gpu219, gpu220, gpu221, gpu222, gpu223, gpu224, gpu225, gpu226, gpu227, gpu228, gpu229, gpu230,
                 gpu231, gpu232, gpu233, gpu234, gpu235, gpu236, gpu237, gpu238, gpu239, gpu240, gpu241, gpu242, gpu243,
                 gpu244, gpu245, gpu246, gpu247, gpu248, gpu249, gpu250, gpu251, gpu252, gpu253, gpu254, gpu255, gpu256,
                 gpu257, gpu258, gpu259, gpu260, gpu261, gpu262, gpu263, gpu264, gpu265, gpu266, gpu267, gpu268, gpu269,
                 gpu270, gpu271, gpu272, gpu273, gpu274, gpu275, gpu276, gpu277, gpu278, gpu279, gpu280, gpu281, gpu282,
                 gpu283, gpu284, gpu285, gpu286, gpu287, gpu288, gpu289, gpu290, gpu291, gpu292, gpu293, gpu294, gpu295,
                 gpu296, gpu297, gpu298, gpu299, gpu300])

        if not Cpu.query.first():  # Check if the Cpu table is empty
            # Add seed data for Cpu
            cpu1 = Cpu(cpu_name="Core i5-10600K", manufacturer="Intel", cpu_brand="Core", cores=6, threads=12,
                       base_clock=3983, boost_clock=5023, socket_type="LGA1200", TDP=105, msrp=396,
                       ReleaseDate=date(2024, 8, 20))
            cpu2 = Cpu(cpu_name="Core i7-14700K", manufacturer="Intel", cpu_brand="Core", cores=16, threads=16,
                       base_clock=4069, boost_clock=5282, socket_type="LGA1151", TDP=105, msrp=712,
                       ReleaseDate=date(2019, 1, 19))
            cpu3 = Cpu(cpu_name="Core i9-12900K", manufacturer="Intel", cpu_brand="Core", cores=4, threads=8,
                       base_clock=3740, boost_clock=4915, socket_type="LGA1200", TDP=105, msrp=589,
                       ReleaseDate=date(2017, 2, 25))
            cpu4 = Cpu(cpu_name="Core i7-13700K", manufacturer="Intel", cpu_brand="Core", cores=12, threads=24,
                       base_clock=3727, boost_clock=4326, socket_type="LGA1151", TDP=125, msrp=751,
                       ReleaseDate=date(2022, 7, 10))
            cpu5 = Cpu(cpu_name="Ryzen 5 5600X", manufacturer="AMD", cpu_brand="Ryzen", cores=12, threads=12,
                       base_clock=3321, boost_clock=4227, socket_type="AM4", TDP=170, msrp=699,
                       ReleaseDate=date(2023, 1, 2))
            cpu6 = Cpu(cpu_name="Ryzen 5 5600X", manufacturer="AMD", cpu_brand="Ryzen", cores=12, threads=12,
                       base_clock=4062, boost_clock=5159, socket_type="AM4", TDP=105, msrp=569,
                       ReleaseDate=date(2022, 12, 27))
            cpu7 = Cpu(cpu_name="Ryzen 5 5600X", manufacturer="AMD", cpu_brand="Ryzen", cores=24, threads=24,
                       base_clock=3209, boost_clock=4131, socket_type="AM4", TDP=95, msrp=685,
                       ReleaseDate=date(2021, 7, 18))
            cpu8 = Cpu(cpu_name="Ryzen 9 7950X", manufacturer="AMD", cpu_brand="Ryzen", cores=4, threads=4,
                       base_clock=3966, boost_clock=4668, socket_type="AM4", TDP=95, msrp=594,
                       ReleaseDate=date(2024, 1, 11))
            cpu9 = Cpu(cpu_name="Core i7-12700K", manufacturer="Intel", cpu_brand="Core", cores=24, threads=24,
                       base_clock=3183, boost_clock=4449, socket_type="LGA1700", TDP=95, msrp=641,
                       ReleaseDate=date(2023, 1, 21))
            cpu10 = Cpu(cpu_name="Ryzen 5 7600X", manufacturer="AMD", cpu_brand="Ryzen", cores=8, threads=8,
                        base_clock=4075, boost_clock=4742, socket_type="AM5", TDP=125, msrp=153,
                        ReleaseDate=date(2019, 9, 19))
            cpu11 = Cpu(cpu_name="Ryzen 7 7700X", manufacturer="AMD", cpu_brand="Ryzen", cores=16, threads=32,
                        base_clock=3954, boost_clock=5192, socket_type="AM5", TDP=105, msrp=271,
                        ReleaseDate=date(2024, 4, 22))
            cpu12 = Cpu(cpu_name="Ryzen 9 3900X", manufacturer="AMD", cpu_brand="Ryzen", cores=12, threads=24,
                        base_clock=3020, boost_clock=3615, socket_type="AM5", TDP=105, msrp=653,
                        ReleaseDate=date(2022, 9, 1))
            cpu13 = Cpu(cpu_name="Core i7-14700K", manufacturer="Intel", cpu_brand="Core", cores=24, threads=48,
                        base_clock=3629, boost_clock=4349, socket_type="LGA1151", TDP=105, msrp=364,
                        ReleaseDate=date(2017, 1, 8))
            cpu14 = Cpu(cpu_name="Core i5-11600K", manufacturer="Intel", cpu_brand="Core", cores=24, threads=48,
                        base_clock=3371, boost_clock=4370, socket_type="LGA1151", TDP=105, msrp=747,
                        ReleaseDate=date(2022, 9, 6))
            cpu15 = Cpu(cpu_name="Ryzen 7 5800X", manufacturer="AMD", cpu_brand="Ryzen", cores=12, threads=12,
                        base_clock=3244, boost_clock=3798, socket_type="AM4", TDP=65, msrp=595,
                        ReleaseDate=date(2021, 6, 10))
            cpu16 = Cpu(cpu_name="Ryzen 5 3600", manufacturer="AMD", cpu_brand="Ryzen", cores=6, threads=12,
                        base_clock=3378, boost_clock=4644, socket_type="AM5", TDP=65, msrp=706,
                        ReleaseDate=date(2022, 5, 18))
            cpu17 = Cpu(cpu_name="Core i9-10850K", manufacturer="Intel", cpu_brand="Core", cores=8, threads=16,
                        base_clock=3210, boost_clock=3910, socket_type="LGA1151", TDP=170, msrp=535,
                        ReleaseDate=date(2019, 1, 11))
            cpu18 = Cpu(cpu_name="Ryzen 7 7700X", manufacturer="AMD", cpu_brand="Ryzen", cores=24, threads=24,
                        base_clock=3800, boost_clock=5298, socket_type="AM5", TDP=125, msrp=376,
                        ReleaseDate=date(2017, 11, 7))
            cpu19 = Cpu(cpu_name="Ryzen 7 7700X", manufacturer="AMD", cpu_brand="Ryzen", cores=6, threads=6,
                        base_clock=3354, boost_clock=3860, socket_type="AM4", TDP=65, msrp=239,
                        ReleaseDate=date(2018, 2, 17))
            cpu20 = Cpu(cpu_name="Ryzen 5 2600", manufacturer="AMD", cpu_brand="Ryzen", cores=8, threads=8,
                        base_clock=3607, boost_clock=4979, socket_type="AM5", TDP=65, msrp=784,
                        ReleaseDate=date(2020, 7, 19))
            cpu21 = Cpu(cpu_name="Ryzen 9 5900X", manufacturer="AMD", cpu_brand="Ryzen", cores=6, threads=12,
                        base_clock=3791, boost_clock=4942, socket_type="AM4", TDP=65, msrp=262,
                        ReleaseDate=date(2021, 12, 15))
            cpu22 = Cpu(cpu_name="Ryzen 5 5600X", manufacturer="AMD", cpu_brand="Ryzen", cores=8, threads=16,
                        base_clock=3503, boost_clock=4791, socket_type="AM5", TDP=170, msrp=182,
                        ReleaseDate=date(2020, 12, 25))
            cpu23 = Cpu(cpu_name="Ryzen 5 7600X", manufacturer="AMD", cpu_brand="Ryzen", cores=16, threads=16,
                        base_clock=4030, boost_clock=5374, socket_type="AM5", TDP=170, msrp=345,
                        ReleaseDate=date(2024, 1, 25))
            cpu24 = Cpu(cpu_name="Core i9-13900K", manufacturer="Intel", cpu_brand="Core", cores=16, threads=16,
                        base_clock=3836, boost_clock=4412, socket_type="LGA1200", TDP=95, msrp=530,
                        ReleaseDate=date(2018, 5, 14))
            cpu25 = Cpu(cpu_name="Core i5-11600K", manufacturer="Intel", cpu_brand="Core", cores=8, threads=16,
                        base_clock=3131, boost_clock=3778, socket_type="LGA1200", TDP=65, msrp=799,
                        ReleaseDate=date(2019, 5, 2))
            cpu26 = Cpu(cpu_name="Core i9-10850K", manufacturer="Intel", cpu_brand="Core", cores=12, threads=12,
                        base_clock=3279, boost_clock=4454, socket_type="LGA1200", TDP=105, msrp=228,
                        ReleaseDate=date(2024, 10, 18))
            cpu27 = Cpu(cpu_name="Ryzen 7 7700X", manufacturer="AMD", cpu_brand="Ryzen", cores=12, threads=24,
                        base_clock=4142, boost_clock=4850, socket_type="AM4", TDP=65, msrp=220,
                        ReleaseDate=date(2017, 4, 11))
            cpu28 = Cpu(cpu_name="Ryzen 9 3900X", manufacturer="AMD", cpu_brand="Ryzen", cores=8, threads=8,
                        base_clock=3915, boost_clock=4678, socket_type="AM5", TDP=95, msrp=614,
                        ReleaseDate=date(2024, 7, 13))
            cpu29 = Cpu(cpu_name="Core i7-10700K", manufacturer="Intel", cpu_brand="Core", cores=16, threads=32,
                        base_clock=4047, boost_clock=5185, socket_type="LGA1200", TDP=95, msrp=521,
                        ReleaseDate=date(2022, 10, 2))
            cpu30 = Cpu(cpu_name="Core i7-11700K", manufacturer="Intel", cpu_brand="Core", cores=8, threads=8,
                        base_clock=3463, boost_clock=4466, socket_type="LGA1200", TDP=65, msrp=420,
                        ReleaseDate=date(2024, 4, 6))
            cpu31 = Cpu(cpu_name="Ryzen 7 3700X", manufacturer="AMD", cpu_brand="Ryzen", cores=24, threads=48,
                        base_clock=3708, boost_clock=4338, socket_type="AM5", TDP=170, msrp=575,
                        ReleaseDate=date(2018, 8, 10))
            cpu32 = Cpu(cpu_name="Core i9-9900K", manufacturer="Intel", cpu_brand="Core", cores=6, threads=6,
                        base_clock=4035, boost_clock=5486, socket_type="LGA1700", TDP=95, msrp=437,
                        ReleaseDate=date(2023, 10, 17))
            cpu33 = Cpu(cpu_name="Core i7-12700K", manufacturer="Intel", cpu_brand="Core", cores=16, threads=32,
                        base_clock=3827, boost_clock=5171, socket_type="LGA1700", TDP=65, msrp=693,
                        ReleaseDate=date(2017, 2, 25))
            cpu34 = Cpu(cpu_name="Core i9-11900K", manufacturer="Intel", cpu_brand="Core", cores=24, threads=48,
                        base_clock=3589, boost_clock=4266, socket_type="LGA1151", TDP=125, msrp=299,
                        ReleaseDate=date(2023, 6, 3))
            cpu35 = Cpu(cpu_name="Core i7-8700K", manufacturer="Intel", cpu_brand="Core", cores=8, threads=8,
                        base_clock=3949, boost_clock=5412, socket_type="LGA1700", TDP=170, msrp=273,
                        ReleaseDate=date(2024, 10, 23))
            cpu36 = Cpu(cpu_name="Core i9-10850K", manufacturer="Intel", cpu_brand="Core", cores=12, threads=12,
                        base_clock=3298, boost_clock=3970, socket_type="LGA1151", TDP=95, msrp=199,
                        ReleaseDate=date(2019, 6, 28))
            cpu37 = Cpu(cpu_name="Core i7-14700K", manufacturer="Intel", cpu_brand="Core", cores=24, threads=48,
                        base_clock=3829, boost_clock=4831, socket_type="LGA1200", TDP=170, msrp=740,
                        ReleaseDate=date(2020, 7, 23))
            cpu38 = Cpu(cpu_name="Ryzen 9 7950X", manufacturer="AMD", cpu_brand="Ryzen", cores=8, threads=16,
                        base_clock=3532, boost_clock=4034, socket_type="AM4", TDP=65, msrp=485,
                        ReleaseDate=date(2024, 11, 25))
            cpu39 = Cpu(cpu_name="Core i7-8700K", manufacturer="Intel", cpu_brand="Core", cores=16, threads=32,
                        base_clock=3001, boost_clock=3873, socket_type="LGA1200", TDP=125, msrp=168,
                        ReleaseDate=date(2024, 7, 17))
            cpu40 = Cpu(cpu_name="Core i7-11700K", manufacturer="Intel", cpu_brand="Core", cores=24, threads=24,
                        base_clock=4023, boost_clock=5466, socket_type="LGA1700", TDP=95, msrp=330,
                        ReleaseDate=date(2017, 10, 20))
            cpu41 = Cpu(cpu_name="Core i5-12600K", manufacturer="Intel", cpu_brand="Core", cores=16, threads=32,
                        base_clock=4154, boost_clock=5033, socket_type="LGA1200", TDP=95, msrp=654,
                        ReleaseDate=date(2018, 7, 9))
            cpu42 = Cpu(cpu_name="Core i7-12700K", manufacturer="Intel", cpu_brand="Core", cores=4, threads=8,
                        base_clock=3815, boost_clock=5077, socket_type="LGA1200", TDP=65, msrp=397,
                        ReleaseDate=date(2021, 11, 23))
            cpu43 = Cpu(cpu_name="Ryzen 9 5900X", manufacturer="AMD", cpu_brand="Ryzen", cores=6, threads=12,
                        base_clock=4050, boost_clock=4836, socket_type="AM4", TDP=170, msrp=357,
                        ReleaseDate=date(2021, 11, 17))
            cpu44 = Cpu(cpu_name="Ryzen 5 3600", manufacturer="AMD", cpu_brand="Ryzen", cores=8, threads=16,
                        base_clock=3478, boost_clock=4766, socket_type="AM4", TDP=170, msrp=741,
                        ReleaseDate=date(2018, 12, 9))
            cpu45 = Cpu(cpu_name="Ryzen 9 3900X", manufacturer="AMD", cpu_brand="Ryzen", cores=4, threads=4,
                        base_clock=3466, boost_clock=4655, socket_type="AM4", TDP=105, msrp=230,
                        ReleaseDate=date(2023, 3, 8))
            cpu46 = Cpu(cpu_name="Core i5-11600K", manufacturer="Intel", cpu_brand="Core", cores=4, threads=8,
                        base_clock=3770, boost_clock=4471, socket_type="LGA1700", TDP=170, msrp=579,
                        ReleaseDate=date(2022, 12, 26))
            cpu47 = Cpu(cpu_name="Core i9-11900K", manufacturer="Intel", cpu_brand="Core", cores=4, threads=8,
                        base_clock=3627, boost_clock=5069, socket_type="LGA1200", TDP=125, msrp=719,
                        ReleaseDate=date(2023, 10, 19))
            cpu48 = Cpu(cpu_name="Ryzen 7 3700X", manufacturer="AMD", cpu_brand="Ryzen", cores=16, threads=16,
                        base_clock=3443, boost_clock=4810, socket_type="AM4", TDP=65, msrp=787,
                        ReleaseDate=date(2022, 1, 7))
            cpu49 = Cpu(cpu_name="Core i7-8700K", manufacturer="Intel", cpu_brand="Core", cores=4, threads=8,
                        base_clock=3098, boost_clock=3906, socket_type="LGA1700", TDP=170, msrp=337,
                        ReleaseDate=date(2022, 8, 14))
            cpu50 = Cpu(cpu_name="Core i7-13700K", manufacturer="Intel", cpu_brand="Core", cores=16, threads=16,
                        base_clock=3738, boost_clock=5083, socket_type="LGA1151", TDP=170, msrp=596,
                        ReleaseDate=date(2017, 11, 26))
            cpu51 = Cpu(cpu_name="Ryzen 9 3900X", manufacturer="AMD", cpu_brand="Ryzen", cores=8, threads=8,
                        base_clock=3408, boost_clock=4572, socket_type="AM5", TDP=65, msrp=370,
                        ReleaseDate=date(2023, 8, 1))
            cpu52 = Cpu(cpu_name="Core i7-10700K", manufacturer="Intel", cpu_brand="Core", cores=12, threads=12,
                        base_clock=4019, boost_clock=5246, socket_type="LGA1700", TDP=125, msrp=315,
                        ReleaseDate=date(2019, 5, 18))
            cpu53 = Cpu(cpu_name="Ryzen 9 3900X", manufacturer="AMD", cpu_brand="Ryzen", cores=4, threads=8,
                        base_clock=3254, boost_clock=4462, socket_type="AM4", TDP=170, msrp=642,
                        ReleaseDate=date(2024, 8, 22))
            cpu54 = Cpu(cpu_name="Core i7-11700K", manufacturer="Intel", cpu_brand="Core", cores=6, threads=12,
                        base_clock=3834, boost_clock=4488, socket_type="LGA1700", TDP=95, msrp=162,
                        ReleaseDate=date(2023, 6, 17))
            cpu55 = Cpu(cpu_name="Core i7-14700K", manufacturer="Intel", cpu_brand="Core", cores=16, threads=16,
                        base_clock=3666, boost_clock=4649, socket_type="LGA1700", TDP=105, msrp=255,
                        ReleaseDate=date(2023, 4, 15))
            cpu56 = Cpu(cpu_name="Core i7-13700K", manufacturer="Intel", cpu_brand="Core", cores=24, threads=48,
                        base_clock=4085, boost_clock=5101, socket_type="LGA1700", TDP=95, msrp=746,
                        ReleaseDate=date(2024, 12, 7))
            cpu57 = Cpu(cpu_name="Ryzen 5 3600", manufacturer="AMD", cpu_brand="Ryzen", cores=24, threads=24,
                        base_clock=3307, boost_clock=4471, socket_type="AM5", TDP=95, msrp=718,
                        ReleaseDate=date(2018, 9, 8))
            cpu58 = Cpu(cpu_name="Ryzen 9 7900X", manufacturer="AMD", cpu_brand="Ryzen", cores=4, threads=4,
                        base_clock=3467, boost_clock=4713, socket_type="AM5", TDP=65, msrp=468,
                        ReleaseDate=date(2017, 12, 25))
            cpu59 = Cpu(cpu_name="Ryzen 9 3900X", manufacturer="AMD", cpu_brand="Ryzen", cores=16, threads=16,
                        base_clock=3876, boost_clock=4660, socket_type="AM5", TDP=170, msrp=440,
                        ReleaseDate=date(2024, 1, 22))
            cpu60 = Cpu(cpu_name="Ryzen 7 7700X", manufacturer="AMD", cpu_brand="Ryzen", cores=16, threads=32,
                        base_clock=3207, boost_clock=4330, socket_type="AM4", TDP=95, msrp=639,
                        ReleaseDate=date(2020, 10, 25))
            cpu61 = Cpu(cpu_name="Core i7-8700K", manufacturer="Intel", cpu_brand="Core", cores=8, threads=16,
                        base_clock=3839, boost_clock=5283, socket_type="LGA1700", TDP=105, msrp=497,
                        ReleaseDate=date(2019, 10, 11))
            cpu62 = Cpu(cpu_name="Ryzen 7 5800X", manufacturer="AMD", cpu_brand="Ryzen", cores=8, threads=8,
                        base_clock=3203, boost_clock=3782, socket_type="AM4", TDP=95, msrp=560,
                        ReleaseDate=date(2020, 7, 16))
            cpu63 = Cpu(cpu_name="Ryzen 5 5600X", manufacturer="AMD", cpu_brand="Ryzen", cores=8, threads=16,
                        base_clock=4034, boost_clock=5049, socket_type="AM5", TDP=170, msrp=785,
                        ReleaseDate=date(2019, 5, 5))
            cpu64 = Cpu(cpu_name="Core i7-10700K", manufacturer="Intel", cpu_brand="Core", cores=12, threads=24,
                        base_clock=3615, boost_clock=4510, socket_type="LGA1200", TDP=125, msrp=468,
                        ReleaseDate=date(2024, 4, 27))
            cpu65 = Cpu(cpu_name="Ryzen 9 3900X", manufacturer="AMD", cpu_brand="Ryzen", cores=8, threads=8,
                        base_clock=4090, boost_clock=4707, socket_type="AM4", TDP=65, msrp=296,
                        ReleaseDate=date(2020, 11, 4))
            cpu66 = Cpu(cpu_name="Core i9-9900K", manufacturer="Intel", cpu_brand="Core", cores=24, threads=24,
                        base_clock=3828, boost_clock=4791, socket_type="LGA1700", TDP=105, msrp=583,
                        ReleaseDate=date(2019, 5, 7))
            cpu67 = Cpu(cpu_name="Ryzen 9 7900X", manufacturer="AMD", cpu_brand="Ryzen", cores=6, threads=6,
                        base_clock=3127, boost_clock=4054, socket_type="AM4", TDP=95, msrp=550,
                        ReleaseDate=date(2023, 5, 6))
            cpu68 = Cpu(cpu_name="Ryzen 7 3700X", manufacturer="AMD", cpu_brand="Ryzen", cores=8, threads=16,
                        base_clock=3773, boost_clock=4483, socket_type="AM5", TDP=95, msrp=314,
                        ReleaseDate=date(2021, 5, 14))
            cpu69 = Cpu(cpu_name="Ryzen 9 5900X", manufacturer="AMD", cpu_brand="Ryzen", cores=12, threads=24,
                        base_clock=4150, boost_clock=5148, socket_type="AM4", TDP=170, msrp=494,
                        ReleaseDate=date(2022, 5, 10))
            cpu70 = Cpu(cpu_name="Ryzen 7 2700X", manufacturer="AMD", cpu_brand="Ryzen", cores=16, threads=16,
                        base_clock=3416, boost_clock=4674, socket_type="AM5", TDP=170, msrp=426,
                        ReleaseDate=date(2023, 2, 3))

            db.session.add_all(
                [cpu1, cpu2, cpu3, cpu4, cpu5, cpu6, cpu7, cpu8, cpu9, cpu10, cpu11, cpu12, cpu13, cpu14, cpu15, cpu16,
                 cpu17, cpu18, cpu19, cpu20, cpu21, cpu22, cpu23, cpu24, cpu25, cpu26, cpu27, cpu28, cpu29, cpu30,
                 cpu31, cpu32, cpu33, cpu34, cpu35, cpu36, cpu37, cpu38, cpu39, cpu40, cpu41, cpu42, cpu43, cpu44,
                 cpu45, cpu46, cpu47, cpu48, cpu49, cpu50, cpu51, cpu52, cpu53, cpu54, cpu55, cpu56, cpu57, cpu58,
                 cpu59, cpu60, cpu61, cpu62, cpu63, cpu64, cpu65, cpu66, cpu67, cpu68, cpu69, cpu70])

        if not Motherboard.query.first():
            # Add seed data for Motherboard
            motherboard1 = Motherboard(motherboard_name="ROG Strix Z490-E Gaming", manufacturer="ASUS",
                                       socket_type="LGA1200", chipset="Z490", form_factor="ATX", max_memory=128,
                                       memory_slots=4, max_memory_speed=5000, msrp=300, ReleaseDate=date(2020, 5, 15))
            motherboard2 = Motherboard(motherboard_name="X570 AORUS XTREME", manufacturer="Gigabyte", socket_type="AM4",
                                       chipset="X570", form_factor="E-ATX", max_memory=128, memory_slots=4,
                                       max_memory_speed=4800, msrp=700, ReleaseDate=date(2019, 7, 7))
            motherboard3 = Motherboard(motherboard_name="MPG Z690 CARBON WIFI", manufacturer="MSI",
                                       socket_type="LGA1700", chipset="Z690", form_factor="ATX", max_memory=128,
                                       memory_slots=4, max_memory_speed=6400, msrp=400, ReleaseDate=date(2021, 11, 4))
            motherboard4 = Motherboard(motherboard_name="B550 AORUS PRO", manufacturer="Gigabyte", socket_type="AM4",
                                       chipset="B550", form_factor="ATX", max_memory=128, memory_slots=4,
                                       max_memory_speed=4866, msrp=180, ReleaseDate=date(2020, 6, 16))
            motherboard5 = Motherboard(motherboard_name="ROG MAXIMUS XIII HERO", manufacturer="ASUS",
                                       socket_type="LGA1200", chipset="Z590", form_factor="ATX", max_memory=128,
                                       memory_slots=4, max_memory_speed=5333, msrp=500, ReleaseDate=date(2021, 1, 11))
            motherboard6 = Motherboard(motherboard_name="TUF GAMING X570-PLUS", manufacturer="ASUS", socket_type="AM4",
                                       chipset="X570", form_factor="ATX", max_memory=128, memory_slots=4,
                                       max_memory_speed=4400, msrp=190, ReleaseDate=date(2019, 7, 7))
            motherboard7 = Motherboard(motherboard_name="MAG B550 TOMAHAWK", manufacturer="MSI", socket_type="AM4",
                                       chipset="B550", form_factor="ATX", max_memory=128, memory_slots=4,
                                       max_memory_speed=4866, msrp=180, ReleaseDate=date(2020, 6, 16))
            motherboard8 = Motherboard(motherboard_name="B660M AORUS PRO", manufacturer="Gigabyte",
                                       socket_type="LGA1700", chipset="B660", form_factor="Micro-ATX", max_memory=128,
                                       memory_slots=4, max_memory_speed=5333, msrp=160, ReleaseDate=date(2022, 1, 4))
            motherboard9 = Motherboard(motherboard_name="X570 Taichi", manufacturer="ASRock", socket_type="AM4",
                                       chipset="X570", form_factor="ATX", max_memory=128, memory_slots=4,
                                       max_memory_speed=4666, msrp=300, ReleaseDate=date(2019, 7, 7))
            motherboard10 = Motherboard(motherboard_name="ROG STRIX B550-F GAMING", manufacturer="ASUS",
                                        socket_type="AM4", chipset="B550", form_factor="ATX", max_memory=128,
                                        memory_slots=4, max_memory_speed=4800, msrp=190, ReleaseDate=date(2020, 6, 16))
            motherboard11 = Motherboard(motherboard_name="Z590 AORUS ULTRA", manufacturer="Gigabyte",
                                        socket_type="LGA1200", chipset="Z590", form_factor="ATX", max_memory=128,
                                        memory_slots=4, max_memory_speed=5400, msrp=330, ReleaseDate=date(2021, 1, 11))
            motherboard12 = Motherboard(motherboard_name="B450 TOMAHAWK MAX", manufacturer="MSI", socket_type="AM4",
                                        chipset="B450", form_factor="ATX", max_memory=64, memory_slots=4,
                                        max_memory_speed=4133, msrp=115, ReleaseDate=date(2019, 7, 7))
            motherboard13 = Motherboard(motherboard_name="ROG STRIX Z690-A GAMING WIFI", manufacturer="ASUS",
                                        socket_type="LGA1700", chipset="Z690", form_factor="ATX", max_memory=128,
                                        memory_slots=4, max_memory_speed=6400, msrp=350, ReleaseDate=date(2021, 11, 4))
            motherboard14 = Motherboard(motherboard_name="X570S AORUS MASTER", manufacturer="Gigabyte",
                                        socket_type="AM4", chipset="X570S", form_factor="ATX", max_memory=128,
                                        memory_slots=4, max_memory_speed=5200, msrp=390, ReleaseDate=date(2021, 7, 7))
            motherboard15 = Motherboard(motherboard_name="Z790 AORUS XTREME", manufacturer="Gigabyte",
                                        socket_type="LGA1700", chipset="Z790", form_factor="E-ATX", max_memory=128,
                                        memory_slots=4, max_memory_speed=7600, msrp=800, ReleaseDate=date(2022, 10, 20))
            motherboard16 = Motherboard(motherboard_name="B550M AORUS PRO-P", manufacturer="Gigabyte",
                                        socket_type="AM4", chipset="B550", form_factor="Micro-ATX", max_memory=128,
                                        memory_slots=4, max_memory_speed=4866, msrp=140, ReleaseDate=date(2020, 6, 16))
            motherboard17 = Motherboard(motherboard_name="PRIME Z690-A", manufacturer="ASUS", socket_type="LGA1700",
                                        chipset="Z690", form_factor="ATX", max_memory=128, memory_slots=4,
                                        max_memory_speed=6000, msrp=290, ReleaseDate=date(2021, 11, 4))
            motherboard18 = Motherboard(motherboard_name="MAG X570 TOMAHAWK WIFI", manufacturer="MSI",
                                        socket_type="AM4", chipset="X570", form_factor="ATX", max_memory=128,
                                        memory_slots=4, max_memory_speed=4600, msrp=220, ReleaseDate=date(2020, 5, 27))
            motherboard19 = Motherboard(motherboard_name="Z590 VISION G", manufacturer="Gigabyte",
                                        socket_type="LGA1200", chipset="Z590", form_factor="ATX", max_memory=128,
                                        memory_slots=4, max_memory_speed=5400, msrp=290, ReleaseDate=date(2021, 1, 11))
            motherboard20 = Motherboard(motherboard_name="ROG STRIX B450-F GAMING II", manufacturer="ASUS",
                                        socket_type="AM4", chipset="B450", form_factor="ATX", max_memory=64,
                                        memory_slots=4, max_memory_speed=4400, msrp=130, ReleaseDate=date(2020, 11, 5))
            motherboard21 = Motherboard(motherboard_name="MPG Z590 GAMING EDGE WIFI", manufacturer="MSI",
                                        socket_type="LGA1200", chipset="Z590", form_factor="ATX", max_memory=128,
                                        memory_slots=4, max_memory_speed=5333, msrp=300, ReleaseDate=date(2021, 1, 11))
            motherboard22 = Motherboard(motherboard_name="B550 VISION D", manufacturer="Gigabyte", socket_type="AM4",
                                        chipset="B550", form_factor="ATX", max_memory=128, memory_slots=4,
                                        max_memory_speed=5200, msrp=260, ReleaseDate=date(2020, 6, 16))
            motherboard23 = Motherboard(motherboard_name="ROG STRIX Z590-E GAMING WIFI", manufacturer="ASUS",
                                        socket_type="LGA1200", chipset="Z590", form_factor="ATX", max_memory=128,
                                        memory_slots=4, max_memory_speed=5333, msrp=380, ReleaseDate=date(2021, 1, 11))
            motherboard24 = Motherboard(motherboard_name="B450M MORTAR MAX", manufacturer="MSI", socket_type="AM4",
                                        chipset="B450", form_factor="Micro-ATX", max_memory=64, memory_slots=4,
                                        max_memory_speed=4133, msrp=105, ReleaseDate=date(2019, 7, 7))
            motherboard25 = Motherboard(motherboard_name="Z690 AORUS MASTER", manufacturer="Gigabyte",
                                        socket_type="LGA1700", chipset="Z690", form_factor="E-ATX", max_memory=128,
                                        memory_slots=4, max_memory_speed=6400, msrp=470, ReleaseDate=date(2021, 11, 4))
            motherboard26 = Motherboard(motherboard_name="X570 UNIFY", manufacturer="MSI", socket_type="AM4",
                                        chipset="X570", form_factor="ATX", max_memory=128, memory_slots=4,
                                        max_memory_speed=4600, msrp=300, ReleaseDate=date(2019, 11, 11))
            motherboard27 = Motherboard(motherboard_name="TUF GAMING B550M-PLUS", manufacturer="ASUS",
                                        socket_type="AM4", chipset="B550", form_factor="Micro-ATX", max_memory=128,
                                        memory_slots=4, max_memory_speed=4600, msrp=160, ReleaseDate=date(2020, 6, 16))
            motherboard28 = Motherboard(motherboard_name="MEG Z690 ACE", manufacturer="MSI", socket_type="LGA1700",
                                        chipset="Z690", form_factor="E-ATX", max_memory=128, memory_slots=4,
                                        max_memory_speed=6666, msrp=600, ReleaseDate=date(2021, 11, 4))
            motherboard29 = Motherboard(motherboard_name="B550 AORUS ELITE", manufacturer="Gigabyte", socket_type="AM4",
                                        chipset="B550", form_factor="ATX", max_memory=128, memory_slots=4,
                                        max_memory_speed=4733, msrp=160, ReleaseDate=date(2020, 6, 16))
            motherboard30 = Motherboard(motherboard_name="ROG CROSSHAIR VIII DARK HERO", manufacturer="ASUS",
                                        socket_type="AM4", chipset="X570", form_factor="ATX", max_memory=128,
                                        memory_slots=4, max_memory_speed=5100, msrp=400, ReleaseDate=date(2020, 11, 5))
            motherboard31 = Motherboard(motherboard_name="Z490 VISION G", manufacturer="Gigabyte",
                                        socket_type="LGA1200", chipset="Z490", form_factor="ATX", max_memory=128,
                                        memory_slots=4, max_memory_speed=5000, msrp=200, ReleaseDate=date(2020, 5, 20))
            motherboard32 = Motherboard(motherboard_name="B660 AORUS MASTER", manufacturer="Gigabyte",
                                        socket_type="LGA1700", chipset="B660", form_factor="ATX", max_memory=128,
                                        memory_slots=4, max_memory_speed=5333, msrp=210, ReleaseDate=date(2022, 1, 4))
            motherboard33 = Motherboard(motherboard_name="ROG STRIX X570-E GAMING", manufacturer="ASUS",
                                        socket_type="AM4", chipset="X570", form_factor="ATX", max_memory=128,
                                        memory_slots=4, max_memory_speed=4800, msrp=330, ReleaseDate=date(2019, 7, 7))
            motherboard34 = Motherboard(motherboard_name="MPG Z490 GAMING CARBON WIFI", manufacturer="MSI",
                                        socket_type="LGA1200", chipset="Z490", form_factor="ATX", max_memory=128,
                                        memory_slots=4, max_memory_speed=5000, msrp=260, ReleaseDate=date(2020, 5, 20))
            motherboard35 = Motherboard(motherboard_name="X570 AORUS ELITE", manufacturer="Gigabyte", socket_type="AM4",
                                        chipset="X570", form_factor="ATX", max_memory=128, memory_slots=4,
                                        max_memory_speed=4400, msrp=200, ReleaseDate=date(2019, 7, 7))
            motherboard36 = Motherboard(motherboard_name="ROG MAXIMUS XII HERO", manufacturer="ASUS",
                                        socket_type="LGA1200", chipset="Z490", form_factor="ATX", max_memory=128,
                                        memory_slots=4, max_memory_speed=4800, msrp=400, ReleaseDate=date(2020, 4, 30))
            motherboard37 = Motherboard(motherboard_name="B550 GAMING X", manufacturer="Gigabyte", socket_type="AM4",
                                        chipset="B550", form_factor="ATX", max_memory=128, memory_slots=4,
                                        max_memory_speed=4733, msrp=140, ReleaseDate=date(2020, 6, 16))
            motherboard38 = Motherboard(motherboard_name="MPG B550 GAMING EDGE WIFI", manufacturer="MSI",
                                        socket_type="AM4", chipset="B550", form_factor="ATX", max_memory=128,
                                        memory_slots=4, max_memory_speed=5100, msrp=180, ReleaseDate=date(2020, 6, 16))
            motherboard39 = Motherboard(motherboard_name="Z590 AORUS PRO AX", manufacturer="Gigabyte",
                                        socket_type="LGA1200", chipset="Z590", form_factor="ATX", max_memory=128,
                                        memory_slots=4, max_memory_speed=5400, msrp=290, ReleaseDate=date(2021, 1, 11))
            motherboard40 = Motherboard(motherboard_name="ROG STRIX B550-I GAMING", manufacturer="ASUS",
                                        socket_type="AM4", chipset="B550", form_factor="Mini-ITX", max_memory=64,
                                        memory_slots=2, max_memory_speed=5100, msrp=230, ReleaseDate=date(2020, 6, 16))
            motherboard41 = Motherboard(motherboard_name="Z690 AORUS ELITE AX", manufacturer="Gigabyte",
                                        socket_type="LGA1700", chipset="Z690", form_factor="ATX", max_memory=128,
                                        memory_slots=4, max_memory_speed=6200, msrp=270, ReleaseDate=date(2021, 11, 4))
            motherboard42 = Motherboard(motherboard_name="X570 PHANTOM GAMING 4", manufacturer="ASRock",
                                        socket_type="AM4", chipset="X570", form_factor="ATX", max_memory=128,
                                        memory_slots=4, max_memory_speed=4066, msrp=155, ReleaseDate=date(2019, 7, 7))
            motherboard43 = Motherboard(motherboard_name="ROG STRIX Z690-I GAMING WIFI", manufacturer="ASUS",
                                        socket_type="LGA1700", chipset="Z690", form_factor="Mini-ITX", max_memory=64,
                                        memory_slots=2, max_memory_speed=6400, msrp=440, ReleaseDate=date(2021, 11, 4))
            motherboard44 = Motherboard(motherboard_name="B550M AORUS ELITE", manufacturer="Gigabyte",
                                        socket_type="AM4", chipset="B550", form_factor="Micro-ATX", max_memory=128,
                                        memory_slots=4, max_memory_speed=4733, msrp=110, ReleaseDate=date(2020, 6, 16))
            motherboard45 = Motherboard(motherboard_name="MPG Z590 GAMING PLUS", manufacturer="MSI",
                                        socket_type="LGA1200", chipset="Z590", form_factor="ATX", max_memory=128,
                                        memory_slots=4, max_memory_speed=5333, msrp=200, ReleaseDate=date(2021, 1, 11))
            motherboard46 = Motherboard(motherboard_name="ROG STRIX Z590-A GAMING WIFI", manufacturer="ASUS",
                                        socket_type="LGA1200", chipset="Z590", form_factor="ATX", max_memory=128,
                                        memory_slots=4, max_memory_speed=5333, msrp=330, ReleaseDate=date(2021, 1, 11))
            motherboard47 = Motherboard(motherboard_name="X570 GAMING X", manufacturer="Gigabyte", socket_type="AM4",
                                        chipset="X570", form_factor="ATX", max_memory=128, memory_slots=4,
                                        max_memory_speed=4400, msrp=170, ReleaseDate=date(2019, 7, 7))
            motherboard48 = Motherboard(motherboard_name="Z790 TAICHI", manufacturer="ASRock", socket_type="LGA1700",
                                        chipset="Z790", form_factor="ATX", max_memory=128, memory_slots=4,
                                        max_memory_speed=7000, msrp=520, ReleaseDate=date(2022, 10, 20))
            motherboard49 = Motherboard(motherboard_name="B550 AORUS MASTER", manufacturer="Gigabyte",
                                        socket_type="AM4", chipset="B550", form_factor="ATX", max_memory=128,
                                        memory_slots=4, max_memory_speed=5200, msrp=280, ReleaseDate=date(2020, 6, 16))
            motherboard50 = Motherboard(motherboard_name="ROG MAXIMUS Z690 FORMULA", manufacturer="ASUS",
                                        socket_type="LGA1700", chipset="Z690", form_factor="ATX", max_memory=128,
                                        memory_slots=4, max_memory_speed=6400, msrp=640, ReleaseDate=date(2021, 11, 4))
            motherboard51 = Motherboard(motherboard_name="B450 AORUS ELITE", manufacturer="Gigabyte", socket_type="AM4",
                                        chipset="B450", form_factor="ATX", max_memory=64, memory_slots=4,
                                        max_memory_speed=3600, msrp=110, ReleaseDate=date(2018, 7, 31))
            motherboard52 = Motherboard(motherboard_name="MPG Z490 GAMING PLUS", manufacturer="MSI",
                                        socket_type="LGA1200", chipset="Z490", form_factor="ATX", max_memory=128,
                                        memory_slots=4, max_memory_speed=4800, msrp=170, ReleaseDate=date(2020, 5, 20))
            motherboard53 = Motherboard(motherboard_name="ROG CROSSHAIR VIII HERO", manufacturer="ASUS",
                                        socket_type="AM4", chipset="X570", form_factor="ATX", max_memory=128,
                                        memory_slots=4, max_memory_speed=4800, msrp=360, ReleaseDate=date(2019, 7, 7))
            motherboard54 = Motherboard(motherboard_name="Z590I AORUS ULTRA", manufacturer="Gigabyte",
                                        socket_type="LGA1200", chipset="Z590", form_factor="Mini-ITX", max_memory=64,
                                        memory_slots=2, max_memory_speed=5333, msrp=280, ReleaseDate=date(2021, 1, 11))
            motherboard55 = Motherboard(motherboard_name="B550I AORUS PRO AX", manufacturer="Gigabyte",
                                        socket_type="AM4", chipset="B550", form_factor="Mini-ITX", max_memory=64,
                                        memory_slots=2, max_memory_speed=5100, msrp=180, ReleaseDate=date(2020, 6, 16))
            motherboard56 = Motherboard(motherboard_name="MEG X570 ACE", manufacturer="MSI", socket_type="AM4",
                                        chipset="X570", form_factor="ATX", max_memory=128, memory_slots=4,
                                        max_memory_speed=4600, msrp=370, ReleaseDate=date(2019, 7, 7))
            motherboard57 = Motherboard(motherboard_name="Z690 GAMING X DDR4", manufacturer="Gigabyte",
                                        socket_type="LGA1700", chipset="Z690", form_factor="ATX", max_memory=128,
                                        memory_slots=4, max_memory_speed=5333, msrp=230, ReleaseDate=date(2021, 11, 4))
            motherboard58 = Motherboard(motherboard_name="PRIME X570-PRO", manufacturer="ASUS", socket_type="AM4",
                                        chipset="X570", form_factor="ATX", max_memory=128, memory_slots=4,
                                        max_memory_speed=4400, msrp=240, ReleaseDate=date(2019, 7, 7))
            motherboard59 = Motherboard(motherboard_name="B660 GAMING X AX DDR4", manufacturer="Gigabyte",
                                        socket_type="LGA1700", chipset="B660", form_factor="ATX", max_memory=128,
                                        memory_slots=4, max_memory_speed=5333, msrp=180, ReleaseDate=date(2022, 1, 4))
            motherboard60 = Motherboard(motherboard_name="ROG STRIX B450-I GAMING", manufacturer="ASUS",
                                        socket_type="AM4", chipset="B450", form_factor="Mini-ITX", max_memory=64,
                                        memory_slots=2, max_memory_speed=3600, msrp=150, ReleaseDate=date(2018, 7, 31))
            motherboard61 = Motherboard(motherboard_name="Z490 AORUS ULTRA", manufacturer="Gigabyte",
                                        socket_type="LGA1200", chipset="Z490", form_factor="ATX", max_memory=128,
                                        memory_slots=4, max_memory_speed=5000, msrp=300, ReleaseDate=date(2020, 5, 20))
            motherboard62 = Motherboard(motherboard_name="MAG B560 TOMAHAWK WIFI", manufacturer="MSI",
                                        socket_type="LGA1200", chipset="B560", form_factor="ATX", max_memory=128,
                                        memory_slots=4, max_memory_speed=5066, msrp=180, ReleaseDate=date(2021, 1, 11))
            motherboard63 = Motherboard(motherboard_name="ROG MAXIMUS Z790 EXTREME", manufacturer="ASUS",
                                        socket_type="LGA1700", chipset="Z790", form_factor="E-ATX", max_memory=128,
                                        memory_slots=4, max_memory_speed=7800, msrp=999, ReleaseDate=date(2022, 10, 20))
            motherboard64 = Motherboard(motherboard_name="X570S GAMING X", manufacturer="Gigabyte", socket_type="AM4",
                                        chipset="X570S", form_factor="ATX", max_memory=128, memory_slots=4,
                                        max_memory_speed=5200, msrp=210, ReleaseDate=date(2021, 7, 7))
            motherboard65 = Motherboard(motherboard_name="PRO Z690-A", manufacturer="MSI", socket_type="LGA1700",
                                        chipset="Z690", form_factor="ATX", max_memory=128, memory_slots=4,
                                        max_memory_speed=6400, msrp=220, ReleaseDate=date(2021, 11, 4))
            motherboard66 = Motherboard(motherboard_name="B450 GAMING PLUS MAX", manufacturer="MSI", socket_type="AM4",
                                        chipset="B450", form_factor="ATX", max_memory=64, memory_slots=4,
                                        max_memory_speed=4133, msrp=100, ReleaseDate=date(2019, 8, 12))
            motherboard67 = Motherboard(motherboard_name="TUF GAMING Z690-PLUS WIFI", manufacturer="ASUS",
                                        socket_type="LGA1700", chipset="Z690", form_factor="ATX", max_memory=128,
                                        memory_slots=4, max_memory_speed=6000, msrp=290, ReleaseDate=date(2021, 11, 4))
            motherboard68 = Motherboard(motherboard_name="X570 PHANTOM GAMING X", manufacturer="ASRock",
                                        socket_type="AM4", chipset="X570", form_factor="ATX", max_memory=128,
                                        memory_slots=4, max_memory_speed=4666, msrp=350, ReleaseDate=date(2019, 7, 7))
            motherboard69 = Motherboard(motherboard_name="Z590 GAMING X", manufacturer="Gigabyte",
                                        socket_type="LGA1200", chipset="Z590", form_factor="ATX", max_memory=128,
                                        memory_slots=4, max_memory_speed=5333, msrp=180, ReleaseDate=date(2021, 1, 11))
            motherboard70 = Motherboard(motherboard_name="ROG STRIX B560-A GAMING WIFI", manufacturer="ASUS",
                                        socket_type="LGA1200", chipset="B560", form_factor="ATX", max_memory=128,
                                        memory_slots=4, max_memory_speed=5000, msrp=180, ReleaseDate=date(2021, 1, 13))
            motherboard71 = Motherboard(motherboard_name="B550 GAMING PLUS", manufacturer="MSI", socket_type="AM4",
                                        chipset="B550", form_factor="ATX", max_memory=128, memory_slots=4,
                                        max_memory_speed=4400, msrp=150, ReleaseDate=date(2020, 6, 16))
            motherboard72 = Motherboard(motherboard_name="Z790 AORUS ELITE AX", manufacturer="Gigabyte",
                                        socket_type="LGA1700", chipset="Z790", form_factor="ATX", max_memory=128,
                                        memory_slots=4, max_memory_speed=7600, msrp=290, ReleaseDate=date(2022, 10, 20))
            motherboard73 = Motherboard(motherboard_name="ROG CROSSHAIR VII HERO", manufacturer="ASUS",
                                        socket_type="AM4", chipset="X470", form_factor="ATX", max_memory=64,
                                        memory_slots=4, max_memory_speed=3600, msrp=280, ReleaseDate=date(2018, 4, 19))
            motherboard74 = Motherboard(motherboard_name="Z490 VISION D", manufacturer="Gigabyte",
                                        socket_type="LGA1200", chipset="Z490", form_factor="ATX", max_memory=128,
                                        memory_slots=4, max_memory_speed=5000, msrp=300, ReleaseDate=date(2020, 5, 20))
            motherboard75 = Motherboard(motherboard_name="MEG Z590 GODLIKE", manufacturer="MSI", socket_type="LGA1200",
                                        chipset="Z590", form_factor="E-ATX", max_memory=128, memory_slots=4,
                                        max_memory_speed=5600, msrp=1000, ReleaseDate=date(2021, 1, 27))
            motherboard76 = Motherboard(motherboard_name="ROG STRIX Z790-F GAMING WIFI", manufacturer="ASUS",
                                        socket_type="LGA1700", chipset="Z790", form_factor="ATX", max_memory=128,
                                        memory_slots=4, max_memory_speed=7600, msrp=460, ReleaseDate=date(2022, 10, 20))
            motherboard77 = Motherboard(motherboard_name="B660M DS3H AX", manufacturer="Gigabyte",
                                        socket_type="LGA1700", chipset="B660", form_factor="Micro-ATX", max_memory=128,
                                        memory_slots=4, max_memory_speed=4800, msrp=130, ReleaseDate=date(2022, 1, 4))
            motherboard78 = Motherboard(motherboard_name="PRIME B550M-A", manufacturer="ASUS", socket_type="AM4",
                                        chipset="B550", form_factor="Micro-ATX", max_memory=128, memory_slots=4,
                                        max_memory_speed=4600, msrp=100, ReleaseDate=date(2020, 6, 16))
            motherboard79 = Motherboard(motherboard_name="Z590 PHANTOM GAMING 4", manufacturer="ASRock",
                                        socket_type="LGA1200", chipset="Z590", form_factor="ATX", max_memory=128,
                                        memory_slots=4, max_memory_speed=4800, msrp=170, ReleaseDate=date(2021, 1, 11))
            motherboard80 = Motherboard(motherboard_name="ROG STRIX X470-F GAMING", manufacturer="ASUS",
                                        socket_type="AM4", chipset="X470", form_factor="ATX", max_memory=64,
                                        memory_slots=4, max_memory_speed=3600, msrp=215, ReleaseDate=date(2018, 4, 19))
            motherboard81 = Motherboard(motherboard_name="MAG B660 TOMAHAWK WIFI", manufacturer="MSI",
                                        socket_type="LGA1700", chipset="B660", form_factor="ATX", max_memory=128,
                                        memory_slots=4, max_memory_speed=4800, msrp=190, ReleaseDate=date(2022, 1, 4))
            motherboard82 = Motherboard(motherboard_name="MPG X570 GAMING PLUS", manufacturer="MSI", socket_type="AM4",
                                        chipset="X570", form_factor="ATX", max_memory=128, memory_slots=4,
                                        max_memory_speed=4400, msrp=170, ReleaseDate=date(2019, 7, 7))
            motherboard83 = Motherboard(motherboard_name="Z690 PHANTOM GAMING 4", manufacturer="ASRock",
                                        socket_type="LGA1700", chipset="Z690", form_factor="ATX", max_memory=128,
                                        memory_slots=4, max_memory_speed=4800, msrp=180, ReleaseDate=date(2021, 11, 4))
            motherboard84 = Motherboard(motherboard_name="X570 AORUS PRO WIFI", manufacturer="Gigabyte",
                                        socket_type="AM4", chipset="X570", form_factor="ATX", max_memory=128,
                                        memory_slots=4, max_memory_speed=4400, msrp=270, ReleaseDate=date(2019, 7, 7))
            motherboard85 = Motherboard(motherboard_name="ROG MAXIMUS Z690 APEX", manufacturer="ASUS",
                                        socket_type="LGA1700", chipset="Z690", form_factor="ATX", max_memory=128,
                                        memory_slots=2, max_memory_speed=6600, msrp=720, ReleaseDate=date(2021, 11, 4))
            motherboard86 = Motherboard(motherboard_name="B450M GAMING PLUS", manufacturer="MSI", socket_type="AM4",
                                        chipset="B450", form_factor="Micro-ATX", max_memory=64, memory_slots=2,
                                        max_memory_speed=3466, msrp=85, ReleaseDate=date(2018, 7, 31))
            motherboard87 = Motherboard(motherboard_name="Z790 PG VELOCITA", manufacturer="ASRock",
                                        socket_type="LGA1700", chipset="Z790", form_factor="ATX", max_memory=128,
                                        memory_slots=4, max_memory_speed=7000, msrp=380, ReleaseDate=date(2022, 10, 20))
            motherboard88 = Motherboard(motherboard_name="B550 PHANTOM GAMING 4", manufacturer="ASRock",
                                        socket_type="AM4", chipset="B550", form_factor="ATX", max_memory=128,
                                        memory_slots=4, max_memory_speed=4533, msrp=115, ReleaseDate=date(2020, 6, 16))
            motherboard89 = Motherboard(motherboard_name="TUF GAMING Z590-PLUS", manufacturer="ASUS",
                                        socket_type="LGA1200", chipset="Z590", form_factor="ATX", max_memory=128,
                                        memory_slots=4, max_memory_speed=5133, msrp=220, ReleaseDate=date(2021, 1, 11))
            motherboard90 = Motherboard(motherboard_name="Z690 UD", manufacturer="Gigabyte", socket_type="LGA1700",
                                        chipset="Z690", form_factor="ATX", max_memory=128, memory_slots=4,
                                        max_memory_speed=5333, msrp=200, ReleaseDate=date(2021, 11, 4))

            # Motherboards from 2017-2018
            motherboard91 = Motherboard(motherboard_name="Z370 AORUS Gaming 7", manufacturer="Gigabyte",
                                        socket_type="LGA1151", chipset="Z370", form_factor="ATX", max_memory=64,
                                        memory_slots=4, max_memory_speed=4000, msrp=250, ReleaseDate=date(2017, 10, 5))
            motherboard92 = Motherboard(motherboard_name="ROG MAXIMUS X HERO", manufacturer="ASUS",
                                        socket_type="LGA1151", chipset="Z370", form_factor="ATX", max_memory=64,
                                        memory_slots=4, max_memory_speed=4133, msrp=280, ReleaseDate=date(2017, 10, 5))
            motherboard93 = Motherboard(motherboard_name="Z370 GAMING PRO CARBON", manufacturer="MSI",
                                        socket_type="LGA1151", chipset="Z370", form_factor="ATX", max_memory=64,
                                        memory_slots=4, max_memory_speed=4000, msrp=190, ReleaseDate=date(2017, 10, 5))
            motherboard94 = Motherboard(motherboard_name="PRIME Z370-A", manufacturer="ASUS", socket_type="LGA1151",
                                        chipset="Z370", form_factor="ATX", max_memory=64, memory_slots=4,
                                        max_memory_speed=4000, msrp=170, ReleaseDate=date(2017, 10, 5))
            motherboard95 = Motherboard(motherboard_name="Z370 Taichi", manufacturer="ASRock", socket_type="LGA1151",
                                        chipset="Z370", form_factor="ATX", max_memory=64, memory_slots=4,
                                        max_memory_speed=4333, msrp=220, ReleaseDate=date(2017, 10, 5))
            motherboard96 = Motherboard(motherboard_name="X399 AORUS Gaming 7", manufacturer="Gigabyte",
                                        socket_type="TR4", chipset="X399", form_factor="ATX", max_memory=128,
                                        memory_slots=8, max_memory_speed=3600, msrp=390, ReleaseDate=date(2017, 8, 10))
            motherboard97 = Motherboard(motherboard_name="ROG ZENITH EXTREME", manufacturer="ASUS", socket_type="TR4",
                                        chipset="X399", form_factor="E-ATX", max_memory=128, memory_slots=8,
                                        max_memory_speed=3600, msrp=550, ReleaseDate=date(2017, 8, 10))
            motherboard98 = Motherboard(motherboard_name="X370 GAMING PRO CARBON", manufacturer="MSI",
                                        socket_type="AM4", chipset="X370", form_factor="ATX", max_memory=64,
                                        memory_slots=4, max_memory_speed=3200, msrp=180, ReleaseDate=date(2017, 3, 2))
            motherboard99 = Motherboard(motherboard_name="PRIME X370-PRO", manufacturer="ASUS", socket_type="AM4",
                                        chipset="X370", form_factor="ATX", max_memory=64, memory_slots=4,
                                        max_memory_speed=3200, msrp=170, ReleaseDate=date(2017, 3, 2))
            motherboard100 = Motherboard(motherboard_name="AB350 GAMING 3", manufacturer="Gigabyte", socket_type="AM4",
                                         chipset="B350", form_factor="ATX", max_memory=64, memory_slots=4,
                                         max_memory_speed=3200, msrp=110, ReleaseDate=date(2017, 3, 2))
            motherboard101 = Motherboard(motherboard_name="ROG CROSSHAIR VI HERO", manufacturer="ASUS",
                                         socket_type="AM4", chipset="X370", form_factor="ATX", max_memory=64,
                                         memory_slots=4, max_memory_speed=3200, msrp=255, ReleaseDate=date(2017, 3, 2))
            motherboard102 = Motherboard(motherboard_name="Z270 GAMING M7", manufacturer="MSI", socket_type="LGA1151",
                                         chipset="Z270", form_factor="ATX", max_memory=64, memory_slots=4,
                                         max_memory_speed=3800, msrp=250, ReleaseDate=date(2017, 1, 5))
            motherboard103 = Motherboard(motherboard_name="ROG MAXIMUS IX FORMULA", manufacturer="ASUS",
                                         socket_type="LGA1151", chipset="Z270", form_factor="ATX", max_memory=64,
                                         memory_slots=4, max_memory_speed=4000, msrp=390, ReleaseDate=date(2017, 1, 5))
            motherboard104 = Motherboard(motherboard_name="Z270 AORUS Gaming 5", manufacturer="Gigabyte",
                                         socket_type="LGA1151", chipset="Z270", form_factor="ATX", max_memory=64,
                                         memory_slots=4, max_memory_speed=3866, msrp=195, ReleaseDate=date(2017, 1, 5))
            motherboard105 = Motherboard(motherboard_name="Z270 Extreme4", manufacturer="ASRock", socket_type="LGA1151",
                                         chipset="Z270", form_factor="ATX", max_memory=64, memory_slots=4,
                                         max_memory_speed=3733, msrp=150, ReleaseDate=date(2017, 1, 5))

            # Most recent motherboards (2023-2024)
            motherboard106 = Motherboard(motherboard_name="ROG STRIX X670E-E GAMING WIFI", manufacturer="ASUS",
                                         socket_type="AM5", chipset="X670E", form_factor="ATX", max_memory=128,
                                         memory_slots=4, max_memory_speed=6400, msrp=500, ReleaseDate=date(2022, 9, 27))
            motherboard107 = Motherboard(motherboard_name="X670E AORUS MASTER", manufacturer="Gigabyte",
                                         socket_type="AM5", chipset="X670E", form_factor="E-ATX", max_memory=128,
                                         memory_slots=4, max_memory_speed=6600, msrp=500, ReleaseDate=date(2022, 9, 27))
            motherboard108 = Motherboard(motherboard_name="MPG X670E CARBON WIFI", manufacturer="MSI",
                                         socket_type="AM5", chipset="X670E", form_factor="ATX", max_memory=128,
                                         memory_slots=4, max_memory_speed=6600, msrp=480, ReleaseDate=date(2022, 9, 27))
            motherboard109 = Motherboard(motherboard_name="B650 AORUS ELITE AX", manufacturer="Gigabyte",
                                         socket_type="AM5", chipset="B650", form_factor="ATX", max_memory=128,
                                         memory_slots=4, max_memory_speed=6600, msrp=240,
                                         ReleaseDate=date(2022, 10, 10))
            motherboard110 = Motherboard(motherboard_name="ROG STRIX B650E-F GAMING WIFI", manufacturer="ASUS",
                                         socket_type="AM5", chipset="B650E", form_factor="ATX", max_memory=128,
                                         memory_slots=4, max_memory_speed=6400, msrp=290,
                                         ReleaseDate=date(2022, 10, 10))
            motherboard111 = Motherboard(motherboard_name="Z790 DARK KINGPIN", manufacturer="EVGA",
                                         socket_type="LGA1700", chipset="Z790", form_factor="E-ATX", max_memory=64,
                                         memory_slots=2, max_memory_speed=8000, msrp=700, ReleaseDate=date(2023, 2, 14))
            motherboard112 = Motherboard(motherboard_name="MAG B650 TOMAHAWK WIFI", manufacturer="MSI",
                                         socket_type="AM5", chipset="B650", form_factor="ATX", max_memory=128,
                                         memory_slots=4, max_memory_speed=6600, msrp=230,
                                         ReleaseDate=date(2022, 10, 10))
            motherboard113 = Motherboard(motherboard_name="Z790 TAICHI CARRARA", manufacturer="ASRock",
                                         socket_type="LGA1700", chipset="Z790", form_factor="ATX", max_memory=128,
                                         memory_slots=4, max_memory_speed=7800, msrp=550,
                                         ReleaseDate=date(2023, 10, 17))
            motherboard114 = Motherboard(motherboard_name="ROG MAXIMUS Z790 DARK HERO", manufacturer="ASUS",
                                         socket_type="LGA1700", chipset="Z790", form_factor="ATX", max_memory=192,
                                         memory_slots=4, max_memory_speed=8000, msrp=700,
                                         ReleaseDate=date(2023, 10, 17))
            motherboard115 = Motherboard(motherboard_name="Z790 AORUS TACHYON X", manufacturer="Gigabyte",
                                         socket_type="LGA1700", chipset="Z790", form_factor="E-ATX", max_memory=96,
                                         memory_slots=2, max_memory_speed=9000, msrp=650,
                                         ReleaseDate=date(2023, 10, 17))
            motherboard116 = Motherboard(motherboard_name="MEG Z790 ACE", manufacturer="MSI", socket_type="LGA1700",
                                         chipset="Z790", form_factor="E-ATX", max_memory=128, memory_slots=4,
                                         max_memory_speed=8000, msrp=650, ReleaseDate=date(2023, 10, 17))
            motherboard117 = Motherboard(motherboard_name="X670E VALKYRIE", manufacturer="ASRock", socket_type="AM5",
                                         chipset="X670E", form_factor="ATX", max_memory=128, memory_slots=4,
                                         max_memory_speed=6600, msrp=450, ReleaseDate=date(2022, 9, 27))
            motherboard118 = Motherboard(motherboard_name="CROSSHAIR X670E GENE", manufacturer="ASUS",
                                         socket_type="AM5", chipset="X670E", form_factor="Micro-ATX", max_memory=64,
                                         memory_slots=2, max_memory_speed=6400, msrp=550, ReleaseDate=date(2022, 9, 27))
            motherboard119 = Motherboard(motherboard_name="B650I AORUS ULTRA", manufacturer="Gigabyte",
                                         socket_type="AM5", chipset="B650", form_factor="Mini-ITX", max_memory=64,
                                         memory_slots=2, max_memory_speed=6600, msrp=240,
                                         ReleaseDate=date(2022, 10, 10))
            motherboard120 = Motherboard(motherboard_name="Z790I AORUS ULTRA", manufacturer="Gigabyte",
                                         socket_type="LGA1700", chipset="Z790", form_factor="Mini-ITX", max_memory=64,
                                         memory_slots=2, max_memory_speed=8000, msrp=380,
                                         ReleaseDate=date(2023, 10, 17))

            db.session.add_all([
                motherboard1, motherboard2, motherboard3, motherboard4, motherboard5,
                motherboard6, motherboard7, motherboard8, motherboard9, motherboard10,
                motherboard11, motherboard12, motherboard13, motherboard14, motherboard15,
                motherboard16, motherboard17, motherboard18, motherboard19, motherboard20,
                motherboard21, motherboard22, motherboard23, motherboard24, motherboard25,
                motherboard26, motherboard27, motherboard28, motherboard29, motherboard30,
                motherboard31, motherboard32, motherboard33, motherboard34, motherboard35,
                motherboard36, motherboard37, motherboard38, motherboard39, motherboard40,
                motherboard41, motherboard42, motherboard43, motherboard44, motherboard45,
                motherboard46, motherboard47, motherboard48, motherboard49, motherboard50,
                motherboard51, motherboard52, motherboard53, motherboard54, motherboard55,
                motherboard56, motherboard57, motherboard58, motherboard59, motherboard60,
                motherboard61, motherboard62, motherboard63, motherboard64, motherboard65,
                motherboard66, motherboard67, motherboard68, motherboard69, motherboard70,
                motherboard71, motherboard72, motherboard73, motherboard74, motherboard75,
                motherboard76, motherboard77, motherboard78, motherboard79, motherboard80,
                motherboard81, motherboard82, motherboard83, motherboard84, motherboard85,
                motherboard86, motherboard87, motherboard88, motherboard89, motherboard90,
                motherboard91, motherboard92, motherboard93, motherboard94, motherboard95,
                motherboard96, motherboard97, motherboard98, motherboard99, motherboard100,
                motherboard101, motherboard102, motherboard103, motherboard104, motherboard105,
                motherboard106, motherboard107, motherboard108, motherboard109, motherboard110,
                motherboard111, motherboard112, motherboard113, motherboard114, motherboard115,
                motherboard116, motherboard117, motherboard118, motherboard119, motherboard120
            ])


        if not Ram.query.first():  # Check if the Ram table is empty
            ram1 = Ram(ram_name="Corsair Vengeance LPX", manufacturer="Corsair", capacity=16, ram_type="DDR4",
                       speed=3200, msrp=79, ReleaseDate=date(2018, 1, 15))
            ram2 = Ram(ram_name="G.Skill Trident Z RGB", manufacturer="G.Skill", capacity=16, ram_type="DDR4",
                       speed=3200, msrp=129, ReleaseDate=date(2018, 2, 5))
            ram3 = Ram(ram_name="HyperX Fury", manufacturer="Kingston", capacity=8, ram_type="DDR4", speed=2666,
                       msrp=45, ReleaseDate=date(2018, 1, 28))
            ram4 = Ram(ram_name="Crucial Ballistix Sport LT", manufacturer="Crucial", capacity=16, ram_type="DDR4",
                       speed=2400, msrp=69, ReleaseDate=date(2018, 3, 10))
            ram5 = Ram(ram_name="Team T-Force Delta RGB", manufacturer="Team Group", capacity=16, ram_type="DDR4",
                       speed=3000, msrp=85, ReleaseDate=date(2018, 2, 25))
            ram6 = Ram(ram_name="Patriot Viper Elite", manufacturer="Patriot", capacity=8, ram_type="DDR4", speed=2400,
                       msrp=42, ReleaseDate=date(2018, 1, 5))
            ram7 = Ram(ram_name="ADATA XPG Spectrix D41", manufacturer="ADATA", capacity=16, ram_type="DDR4",
                       speed=3000, msrp=89, ReleaseDate=date(2018, 4, 12))
            ram8 = Ram(ram_name="GeIL EVO POTENZA", manufacturer="GeIL", capacity=16, ram_type="DDR4", speed=2400,
                       msrp=65, ReleaseDate=date(2018, 3, 22))
            ram9 = Ram(ram_name="Corsair Dominator Platinum", manufacturer="Corsair", capacity=16, ram_type="DDR4",
                       speed=3600, msrp=159, ReleaseDate=date(2018, 5, 3))
            ram10 = Ram(ram_name="G.Skill Ripjaws V", manufacturer="G.Skill", capacity=16, ram_type="DDR4", speed=3200,
                        msrp=74, ReleaseDate=date(2018, 4, 19))
            ram11 = Ram(ram_name="Crucial Ballistix Elite", manufacturer="Crucial", capacity=32, ram_type="DDR4",
                        speed=3200, msrp=189, ReleaseDate=date(2018, 6, 7))
            ram12 = Ram(ram_name="Kingston HyperX Predator", manufacturer="Kingston", capacity=16, ram_type="DDR4",
                        speed=3200, msrp=119, ReleaseDate=date(2018, 5, 15))
            ram13 = Ram(ram_name="Team T-Force Vulcan", manufacturer="Team Group", capacity=8, ram_type="DDR4",
                        speed=2666, msrp=39, ReleaseDate=date(2018, 7, 2))
            ram14 = Ram(ram_name="Patriot Viper Steel", manufacturer="Patriot", capacity=16, ram_type="DDR4",
                        speed=3000, msrp=79, ReleaseDate=date(2018, 6, 18))
            ram15 = Ram(ram_name="ADATA XPG Z1", manufacturer="ADATA", capacity=8, ram_type="DDR4", speed=2666, msrp=42,
                        ReleaseDate=date(2018, 7, 25))
            ram16 = Ram(ram_name="G.Skill Flare X", manufacturer="G.Skill", capacity=16, ram_type="DDR4", speed=3200,
                        msrp=109, ReleaseDate=date(2018, 8, 10))
            ram17 = Ram(ram_name="Corsair Vengeance RGB PRO", manufacturer="Corsair", capacity=16, ram_type="DDR4",
                        speed=3200, msrp=99, ReleaseDate=date(2018, 7, 12))
            ram18 = Ram(ram_name="Crucial Ballistix Tactical", manufacturer="Crucial", capacity=16, ram_type="DDR4",
                        speed=3000, msrp=89, ReleaseDate=date(2018, 8, 27))
            ram19 = Ram(ram_name="Kingston HyperX Fury RGB", manufacturer="Kingston", capacity=16, ram_type="DDR4",
                        speed=3200, msrp=94, ReleaseDate=date(2018, 9, 5))
            ram20 = Ram(ram_name="Team T-Force Night Hawk", manufacturer="Team Group", capacity=16, ram_type="DDR4",
                        speed=3200, msrp=109, ReleaseDate=date(2018, 8, 19))
            ram21 = Ram(ram_name="GeIL Super Luce RGB", manufacturer="GeIL", capacity=16, ram_type="DDR4", speed=3000,
                        msrp=95, ReleaseDate=date(2018, 10, 3))
            ram22 = Ram(ram_name="Patriot Viper RGB", manufacturer="Patriot", capacity=16, ram_type="DDR4", speed=3200,
                        msrp=99, ReleaseDate=date(2018, 9, 21))
            ram23 = Ram(ram_name="ADATA XPG GAMMIX D10", manufacturer="ADATA", capacity=16, ram_type="DDR4", speed=2666,
                        msrp=69, ReleaseDate=date(2018, 10, 15))
            ram24 = Ram(ram_name="G.Skill Trident Z Royal", manufacturer="G.Skill", capacity=16, ram_type="DDR4",
                        speed=3600, msrp=169, ReleaseDate=date(2018, 11, 8))
            ram25 = Ram(ram_name="Corsair Vengeance RGB PRO SL", manufacturer="Corsair", capacity=32, ram_type="DDR4",
                        speed=3600, msrp=199, ReleaseDate=date(2018, 10, 29))
            ram26 = Ram(ram_name="Crucial Ballistix MAX", manufacturer="Crucial", capacity=16, ram_type="DDR4",
                        speed=4000, msrp=149, ReleaseDate=date(2018, 11, 20))
            ram27 = Ram(ram_name="Kingston HyperX Fury Black", manufacturer="Kingston", capacity=8, ram_type="DDR4",
                        speed=2666, msrp=49, ReleaseDate=date(2018, 12, 5))
            ram28 = Ram(ram_name="Team T-Force XTREEM", manufacturer="Team Group", capacity=16, ram_type="DDR4",
                        speed=4133, msrp=189, ReleaseDate=date(2018, 11, 27))
            ram29 = Ram(ram_name="Patriot Viper 4", manufacturer="Patriot", capacity=8, ram_type="DDR4", speed=3000,
                        msrp=52, ReleaseDate=date(2018, 12, 17))
            ram30 = Ram(ram_name="ADATA XPG SPECTRIX D80", manufacturer="ADATA", capacity=16, ram_type="DDR4",
                        speed=3600, msrp=139, ReleaseDate=date(2018, 12, 28))
            ram31 = Ram(ram_name="Corsair Vengeance LPX", manufacturer="Corsair", capacity=32, ram_type="DDR4",
                        speed=3200, msrp=159, ReleaseDate=date(2019, 1, 10))
            ram32 = Ram(ram_name="G.Skill Ripjaws 4", manufacturer="G.Skill", capacity=16, ram_type="DDR4", speed=3000,
                        msrp=85, ReleaseDate=date(2019, 1, 25))
            ram33 = Ram(ram_name="Kingston HyperX Impact", manufacturer="Kingston", capacity=16, ram_type="DDR4",
                        speed=2400, msrp=79, ReleaseDate=date(2019, 2, 7))
            ram34 = Ram(ram_name="Crucial Ballistix Sport AT", manufacturer="Crucial", capacity=16, ram_type="DDR4",
                        speed=3000, msrp=84, ReleaseDate=date(2019, 1, 18))
            ram35 = Ram(ram_name="Team T-Force Dark Pro", manufacturer="Team Group", capacity=16, ram_type="DDR4",
                        speed=3200, msrp=95, ReleaseDate=date(2019, 2, 20))
            ram36 = Ram(ram_name="GeIL Evo X II", manufacturer="GeIL", capacity=16, ram_type="DDR4", speed=3000,
                        msrp=89, ReleaseDate=date(2019, 3, 5))
            ram37 = Ram(ram_name="Patriot Viper Steel RGB", manufacturer="Patriot", capacity=32, ram_type="DDR4",
                        speed=3200, msrp=175, ReleaseDate=date(2019, 2, 27))
            ram38 = Ram(ram_name="ADATA XPG SPECTRIX D60G", manufacturer="ADATA", capacity=16, ram_type="DDR4",
                        speed=3200, msrp=109, ReleaseDate=date(2019, 3, 15))
            ram39 = Ram(ram_name="G.Skill Trident Z Neo", manufacturer="G.Skill", capacity=32, ram_type="DDR4",
                        speed=3600, msrp=199, ReleaseDate=date(2019, 4, 2))
            ram40 = Ram(ram_name="Corsair Vengeance RGB PRO TUF", manufacturer="Corsair", capacity=16, ram_type="DDR4",
                        speed=3200, msrp=104, ReleaseDate=date(2019, 3, 28))
            ram41 = Ram(ram_name="Crucial Ballistix Tracer RGB", manufacturer="Crucial", capacity=16, ram_type="DDR4",
                        speed=3200, msrp=119, ReleaseDate=date(2019, 4, 18))
            ram42 = Ram(ram_name="Kingston HyperX Predator RGB", manufacturer="Kingston", capacity=32, ram_type="DDR4",
                        speed=3600, msrp=219, ReleaseDate=date(2019, 5, 3))
            ram43 = Ram(ram_name="Team T-Force Delta R", manufacturer="Team Group", capacity=16, ram_type="DDR4",
                        speed=3000, msrp=89, ReleaseDate=date(2019, 4, 25))
            ram44 = Ram(ram_name="Patriot Viper 4 Blackout", manufacturer="Patriot", capacity=16, ram_type="DDR4",
                        speed=3200, msrp=75, ReleaseDate=date(2019, 5, 14))
            ram45 = Ram(ram_name="ADATA XPG SPECTRIX D50", manufacturer="ADATA", capacity=16, ram_type="DDR4",
                        speed=3600, msrp=129, ReleaseDate=date(2019, 5, 28))
            ram46 = Ram(ram_name="G.Skill Trident Z Royal Elite", manufacturer="G.Skill", capacity=32, ram_type="DDR4",
                        speed=4000, msrp=299, ReleaseDate=date(2019, 6, 10))
            ram47 = Ram(ram_name="Corsair Dominator Platinum RGB", manufacturer="Corsair", capacity=32, ram_type="DDR4",
                        speed=3600, msrp=259, ReleaseDate=date(2019, 5, 22))
            ram48 = Ram(ram_name="Crucial Ballistix Black", manufacturer="Crucial", capacity=16, ram_type="DDR4",
                        speed=3200, msrp=89, ReleaseDate=date(2019, 6, 25))
            ram49 = Ram(ram_name="Kingston HyperX Fury RGB", manufacturer="Kingston", capacity=32, ram_type="DDR4",
                        speed=3200, msrp=169, ReleaseDate=date(2019, 7, 8))
            ram50 = Ram(ram_name="Team T-Force Xcalibur", manufacturer="Team Group", capacity=16, ram_type="DDR4",
                        speed=4000, msrp=159, ReleaseDate=date(2019, 6, 19))
            ram51 = Ram(ram_name="GeIL Orion RGB", manufacturer="GeIL", capacity=16, ram_type="DDR4", speed=3600,
                        msrp=119, ReleaseDate=date(2019, 7, 22))
            ram52 = Ram(ram_name="Patriot Viper Steel Series", manufacturer="Patriot", capacity=64, ram_type="DDR4",
                        speed=3200, msrp=289, ReleaseDate=date(2019, 8, 5))
            ram53 = Ram(ram_name="ADATA XPG SPECTRIX D41 TUF", manufacturer="ADATA", capacity=16, ram_type="DDR4",
                        speed=3200, msrp=99, ReleaseDate=date(2019, 7, 17))
            ram54 = Ram(ram_name="G.Skill Sniper X", manufacturer="G.Skill", capacity=16, ram_type="DDR4", speed=3200,
                        msrp=89, ReleaseDate=date(2019, 8, 20))
            ram55 = Ram(ram_name="Corsair Vengeance LPX Black", manufacturer="Corsair", capacity=64, ram_type="DDR4",
                        speed=3200, msrp=299, ReleaseDate=date(2019, 9, 3))
            ram56 = Ram(ram_name="Crucial Ballistix White RGB", manufacturer="Crucial", capacity=32, ram_type="DDR4",
                        speed=3600, msrp=179, ReleaseDate=date(2019, 8, 15))
            ram57 = Ram(ram_name="Kingston HyperX Fury Bronze", manufacturer="Kingston", capacity=16, ram_type="DDR4",
                        speed=3200, msrp=85, ReleaseDate=date(2019, 9, 17))
            ram58 = Ram(ram_name="Team T-Force Dark Z", manufacturer="Team Group", capacity=16, ram_type="DDR4",
                        speed=3200, msrp=72, ReleaseDate=date(2019, 10, 1))
            ram59 = Ram(ram_name="Patriot Signature Line", manufacturer="Patriot", capacity=8, ram_type="DDR4",
                        speed=2666, msrp=35, ReleaseDate=date(2019, 9, 12))
            ram60 = Ram(ram_name="ADATA Premier", manufacturer="ADATA", capacity=8, ram_type="DDR4", speed=2666,
                        msrp=32, ReleaseDate=date(2019, 10, 15))
            ram61 = Ram(ram_name="G.Skill Aegis", manufacturer="G.Skill", capacity=16, ram_type="DDR4", speed=3000,
                        msrp=58, ReleaseDate=date(2019, 11, 4))
            ram62 = Ram(ram_name="Corsair LPX Vengeance White", manufacturer="Corsair", capacity=32, ram_type="DDR4",
                        speed=3600, msrp=165, ReleaseDate=date(2019, 10, 21))
            ram63 = Ram(ram_name="Crucial CT16G4DFR", manufacturer="Crucial", capacity=16, ram_type="DDR4", speed=2666,
                        msrp=55, ReleaseDate=date(2019, 11, 18))
            ram64 = Ram(ram_name="Kingston ValueRAM", manufacturer="Kingston", capacity=8, ram_type="DDR4", speed=2400,
                        msrp=30, ReleaseDate=date(2019, 12, 2))
            ram65 = Ram(ram_name="Team Elite Plus", manufacturer="Team Group", capacity=8, ram_type="DDR4", speed=2400,
                        msrp=29, ReleaseDate=date(2019, 11, 14))
            ram66 = Ram(ram_name="GeIL Dragon RAM", manufacturer="GeIL", capacity=16, ram_type="DDR4", speed=3000,
                        msrp=69, ReleaseDate=date(2019, 12, 16))
            ram67 = Ram(ram_name="Patriot Signature Premium", manufacturer="Patriot", capacity=16, ram_type="DDR4",
                        speed=2666, msrp=59, ReleaseDate=date(2019, 12, 30))
            ram68 = Ram(ram_name="ADATA XPG Hunter", manufacturer="ADATA", capacity=16, ram_type="DDR4", speed=3000,
                        msrp=65, ReleaseDate=date(2020, 1, 14))
            ram69 = Ram(ram_name="G.Skill Trident Z RGB DC", manufacturer="G.Skill", capacity=64, ram_type="DDR4",
                        speed=3200, msrp=329, ReleaseDate=date(2020, 1, 28))
            ram70 = Ram(ram_name="Corsair Vengeance RGB RT", manufacturer="Corsair", capacity=16, ram_type="DDR4",
                        speed=3600, msrp=119, ReleaseDate=date(2020, 2, 12))
            ram71 = Ram(ram_name="Crucial Ballistix Gaming", manufacturer="Crucial", capacity=16, ram_type="DDR4",
                        speed=3600, msrp=89, ReleaseDate=date(2020, 1, 18))
            ram72 = Ram(ram_name="Kingston HyperX Beast", manufacturer="Kingston", capacity=32, ram_type="DDR4",
                        speed=3600, msrp=175, ReleaseDate=date(2020, 2, 27))
            ram73 = Ram(ram_name="Team T-Force Night Hawk Legend", manufacturer="Team Group", capacity=16,
                        ram_type="DDR4", speed=3600, msrp=129, ReleaseDate=date(2020, 3, 10))
            ram74 = Ram(ram_name="Patriot Viper VPR100", manufacturer="Patriot", capacity=16, ram_type="DDR4",
                        speed=3600, msrp=115, ReleaseDate=date(2020, 2, 20))
            ram75 = Ram(ram_name="ADATA XPG Lancer", manufacturer="ADATA", capacity=16, ram_type="DDR4", speed=4000,
                        msrp=139, ReleaseDate=date(2020, 3, 25))
            ram76 = Ram(ram_name="G.Skill Ripjaws S5", manufacturer="G.Skill", capacity=32, ram_type="DDR4", speed=3600,
                        msrp=159, ReleaseDate=date(2020, 4, 7))
            ram77 = Ram(ram_name="Corsair Dominator Airflow", manufacturer="Corsair", capacity=32, ram_type="DDR4",
                        speed=4000, msrp=259, ReleaseDate=date(2020, 3, 17))
            ram78 = Ram(ram_name="Crucial Ballistix MAX RGB", manufacturer="Crucial", capacity=32, ram_type="DDR4",
                        speed=4000, msrp=229, ReleaseDate=date(2020, 4, 21))
            ram79 = Ram(ram_name="Kingston HyperX Renegade", manufacturer="Kingston", capacity=16, ram_type="DDR4",
                        speed=4266, msrp=169, ReleaseDate=date(2020, 5, 5))
            ram80 = Ram(ram_name="Team T-Force Xtreem ARGB", manufacturer="Team Group", capacity=16, ram_type="DDR4",
                        speed=4500, msrp=189, ReleaseDate=date(2020, 4, 14))
            ram81 = Ram(ram_name="GeIL Polaris RGB", manufacturer="GeIL", capacity=16, ram_type="DDR4", speed=3600,
                        msrp=109, ReleaseDate=date(2020, 5, 19))
            ram82 = Ram(ram_name="Patriot Viper 4000", manufacturer="Patriot", capacity=32, ram_type="DDR4", speed=4000,
                        msrp=219, ReleaseDate=date(2020, 6, 2))
            ram83 = Ram(ram_name="ADATA XPG D50 Xtreme", manufacturer="ADATA", capacity=32, ram_type="DDR4", speed=4133,
                        msrp=249, ReleaseDate=date(2020, 5, 12))
            ram84 = Ram(ram_name="G.Skill Trident Z Neo Special", manufacturer="G.Skill", capacity=64, ram_type="DDR4",
                        speed=3600, msrp=349, ReleaseDate=date(2020, 6, 16))
            ram85 = Ram(ram_name="Corsair Vengeance Pro SL", manufacturer="Corsair", capacity=32, ram_type="DDR4",
                        speed=3600, msrp=169, ReleaseDate=date(2020, 7, 1))
            ram86 = Ram(ram_name="Crucial Ballistix Red RGB", manufacturer="Crucial", capacity=32, ram_type="DDR4",
                        speed=3200, msrp=149, ReleaseDate=date(2020, 6, 10))
            ram87 = Ram(ram_name="Kingston HyperX Predator OC", manufacturer="Kingston", capacity=32, ram_type="DDR4",
                        speed=4400, msrp=289, ReleaseDate=date(2020, 7, 15))
            ram88 = Ram(ram_name="Team Group Zeus", manufacturer="Team Group", capacity=16, ram_type="DDR4", speed=3000,
                        msrp=62, ReleaseDate=date(2020, 7, 29))
            ram89 = Ram(ram_name="Patriot Viper Elite II", manufacturer="Patriot", capacity=16, ram_type="DDR4",
                        speed=3600, msrp=95, ReleaseDate=date(2020, 8, 11))
            ram90 = Ram(ram_name="ADATA XPG Spectrix D50G", manufacturer="ADATA", capacity=32, ram_type="DDR4",
                        speed=3600, msrp=179, ReleaseDate=date(2020, 7, 20))
            ram91 = Ram(ram_name="G.Skill Trident Z Royal Gold", manufacturer="G.Skill", capacity=32, ram_type="DDR4",
                        speed=4000, msrp=279, ReleaseDate=date(2020, 8, 25))
            ram92 = Ram(ram_name="Corsair Vengeance RGB Pro SL", manufacturer="Corsair", capacity=32, ram_type="DDR4",
                        speed=3600, msrp=169, ReleaseDate=date(2020, 9, 8))
            ram93 = Ram(ram_name="Crucial Ballistix MAX Black", manufacturer="Crucial", capacity=32, ram_type="DDR4",
                        speed=4400, msrp=249, ReleaseDate=date(2020, 8, 14))
            ram94 = Ram(ram_name="Kingston HyperX Fury Beast", manufacturer="Kingston", capacity=32, ram_type="DDR4",
                        speed=3600, msrp=159, ReleaseDate=date(2020, 9, 22))
            ram95 = Ram(ram_name="Team T-Force Delta RGB White", manufacturer="Team Group", capacity=32,
                        ram_type="DDR4", speed=3200, msrp=135, ReleaseDate=date(2020, 10, 6))
            ram96 = Ram(ram_name="GeIL Orion AMD Edition", manufacturer="GeIL", capacity=16, ram_type="DDR4",
                        speed=3600, msrp=105, ReleaseDate=date(2020, 9, 17))
            ram97 = Ram(ram_name="Patriot Viper Steel RGB", manufacturer="Patriot", capacity=32, ram_type="DDR4",
                        speed=3600, msrp=169, ReleaseDate=date(2020, 10, 20))
            ram98 = Ram(ram_name="ADATA XPG GAMMIX D20", manufacturer="ADATA", capacity=16, ram_type="DDR4", speed=3600,
                        msrp=95, ReleaseDate=date(2020, 11, 3))
            ram99 = Ram(ram_name="G.Skill Ripjaws V Black", manufacturer="G.Skill", capacity=64, ram_type="DDR4",
                        speed=3600, msrp=259, ReleaseDate=date(2020, 10, 15))
            ram100 = Ram(ram_name="Corsair Vengeance LPX High Performance", manufacturer="Corsair", capacity=16,
                         ram_type="DDR4", speed=4600, msrp=189, ReleaseDate=date(2020, 11, 17))
            ram101 = Ram(ram_name="Crucial Ballistix Ultra", manufacturer="Crucial", capacity=32, ram_type="DDR4",
                         speed=4800, msrp=299, ReleaseDate=date(2020, 12, 1))
            ram102 = Ram(ram_name="Kingston HyperX Fury Special Edition", manufacturer="Kingston", capacity=32,
                         ram_type="DDR4", speed=3733, msrp=179, ReleaseDate=date(2020, 11, 12))
            ram103 = Ram(ram_name="Team T-Force Vulcan Z", manufacturer="Team Group", capacity=32, ram_type="DDR4",
                         speed=3200, msrp=115, ReleaseDate=date(2020, 12, 15))
            ram104 = Ram(ram_name="Patriot Viper 4 Blackout Series", manufacturer="Patriot", capacity=16,
                         ram_type="DDR4", speed=4133, msrp=129, ReleaseDate=date(2020, 12, 29))
            ram105 = Ram(ram_name="ADATA XPG Spectrix D45G", manufacturer="ADATA", capacity=32, ram_type="DDR4",
                         speed=3600, msrp=159, ReleaseDate=date(2021, 1, 12))
            ram106 = Ram(ram_name="G.Skill Trident Z Royal Silver", manufacturer="G.Skill", capacity=32,
                         ram_type="DDR4", speed=4266, msrp=289, ReleaseDate=date(2021, 1, 26))
            ram107 = Ram(ram_name="Corsair Dominator Platinum White", manufacturer="Corsair", capacity=32,
                         ram_type="DDR4", speed=4000, msrp=249, ReleaseDate=date(2021, 2, 9))
            ram108 = Ram(ram_name="Crucial Ballistix Tactical Tracer", manufacturer="Crucial", capacity=32,
                         ram_type="DDR4", speed=3600, msrp=179, ReleaseDate=date(2021, 1, 19))
            ram109 = Ram(ram_name="Kingston FURY Beast", manufacturer="Kingston", capacity=32, ram_type="DDR4",
                         speed=3200, msrp=145, ReleaseDate=date(2021, 2, 23))
            ram110 = Ram(ram_name="Team T-Force XTREEM ARGB White", manufacturer="Team Group", capacity=32,
                         ram_type="DDR4", speed=3600, msrp=189, ReleaseDate=date(2021, 3, 9))
            ram111 = Ram(ram_name="GeIL EVO X III", manufacturer="GeIL", capacity=32, ram_type="DDR4", speed=3600,
                         msrp=159, ReleaseDate=date(2021, 2, 16))
            ram112 = Ram(ram_name="Patriot Viper RGB White", manufacturer="Patriot", capacity=32, ram_type="DDR4",
                         speed=3600, msrp=165, ReleaseDate=date(2021, 3, 23))
            ram113 = Ram(ram_name="ADATA XPG Lancer RGB", manufacturer="ADATA", capacity=32, ram_type="DDR4",
                         speed=3600, msrp=169, ReleaseDate=date(2021, 4, 6))
            ram114 = Ram(ram_name="G.Skill Trident Z Royal Elite Gold", manufacturer="G.Skill", capacity=32,
                         ram_type="DDR4", speed=4800, msrp=339, ReleaseDate=date(2021, 3, 18))
            ram115 = Ram(ram_name="Corsair Vengeance RGB RT Black", manufacturer="Corsair", capacity=32,
                         ram_type="DDR4", speed=3600, msrp=175, ReleaseDate=date(2021, 4, 20))
            ram116 = Ram(ram_name="Crucial Ballistix MAX White", manufacturer="Crucial", capacity=32, ram_type="DDR4",
                         speed=4000, msrp=209, ReleaseDate=date(2021, 5, 4))
            ram117 = Ram(ram_name="Kingston FURY Renegade", manufacturer="Kingston", capacity=32, ram_type="DDR4",
                         speed=4600, msrp=279, ReleaseDate=date(2021, 4, 15))
            ram118 = Ram(ram_name="Team T-Force XTREEM Mirror", manufacturer="Team Group", capacity=32, ram_type="DDR4",
                         speed=3600, msrp=185, ReleaseDate=date(2021, 5, 18))
            ram119 = Ram(ram_name="Patriot Viper 4000 Elite", manufacturer="Patriot", capacity=32, ram_type="DDR4",
                         speed=4000, msrp=219, ReleaseDate=date(2021, 6, 1))
            ram120 = Ram(ram_name="ADATA XPG CASTER RGB", manufacturer="ADATA", capacity=32, ram_type="DDR4",
                         speed=3600, msrp=175, ReleaseDate=date(2021, 5, 11))
            ram121 = Ram(ram_name="G.Skill Trident Z RGB Crystal", manufacturer="G.Skill", capacity=32, ram_type="DDR4",
                         speed=3600, msrp=199, ReleaseDate=date(2021, 6, 15))
            ram122 = Ram(ram_name="Corsair Dominator Platinum Special", manufacturer="Corsair", capacity=32,
                         ram_type="DDR4", speed=4000, msrp=259, ReleaseDate=date(2021, 7, 1))
            ram123 = Ram(ram_name="Crucial Ballistix Gaming X", manufacturer="Crucial", capacity=32, ram_type="DDR4",
                         speed=3600, msrp=169, ReleaseDate=date(2021, 6, 10))
            ram124 = Ram(ram_name="Kingston FURY Beast White RGB", manufacturer="Kingston", capacity=32,
                         ram_type="DDR4", speed=3600, msrp=179, ReleaseDate=date(2021, 7, 13))
            ram125 = Ram(ram_name="Team T-Force Cardea Frosted", manufacturer="Team Group", capacity=32,
                         ram_type="DDR4", speed=3600, msrp=175, ReleaseDate=date(2021, 7, 27))
            ram126 = Ram(ram_name="GeIL Polaris White RGB", manufacturer="GeIL", capacity=32, ram_type="DDR4",
                         speed=3600, msrp=165, ReleaseDate=date(2021, 8, 10))
            ram127 = Ram(ram_name="Patriot Viper Steel RGB Pro", manufacturer="Patriot", capacity=32, ram_type="DDR4",
                         speed=3600, msrp=175, ReleaseDate=date(2021, 7, 20))
            ram128 = Ram(ram_name="ADATA XPG Spectrix D45", manufacturer="ADATA", capacity=32, ram_type="DDR4",
                         speed=3600, msrp=169, ReleaseDate=date(2021, 8, 24))
            ram129 = Ram(ram_name="G.Skill Ripjaws V OC", manufacturer="G.Skill", capacity=32, ram_type="DDR4",
                         speed=4000, msrp=209, ReleaseDate=date(2021, 9, 7))
            ram130 = Ram(ram_name="Corsair Vengeance LPX Ultra", manufacturer="Corsair", capacity=64, ram_type="DDR4",
                         speed=3600, msrp=289, ReleaseDate=date(2021, 8, 17))
            ram131 = Ram(ram_name="Crucial Ballistix RGB Gaming", manufacturer="Crucial", capacity=32, ram_type="DDR4",
                         speed=3600, msrp=169, ReleaseDate=date(2021, 9, 21))
            ram132 = Ram(ram_name="Kingston FURY Impact", manufacturer="Kingston", capacity=32, ram_type="DDR4",
                         speed=3200, msrp=155, ReleaseDate=date(2021, 10, 5))
            ram133 = Ram(ram_name="Team T-Force DELTA MAX RGB", manufacturer="Team Group", capacity=32, ram_type="DDR4",
                         speed=3600, msrp=179, ReleaseDate=date(2021, 9, 14))
            ram134 = Ram(ram_name="GeIL Orion Phantom Gaming", manufacturer="GeIL", capacity=32, ram_type="DDR4",
                         speed=3600, msrp=175, ReleaseDate=date(2021, 10, 19))
            ram135 = Ram(ram_name="Patriot Viper Elite II RGB", manufacturer="Patriot", capacity=32, ram_type="DDR4",
                         speed=3600, msrp=175, ReleaseDate=date(2021, 11, 2))
            ram136 = Ram(ram_name="ADATA XPG GAMMIX D45G", manufacturer="ADATA", capacity=32, ram_type="DDR4",
                         speed=3600, msrp=169, ReleaseDate=date(2021, 10, 12))
            ram137 = Ram(ram_name="G.Skill Trident Z Neo OC", manufacturer="G.Skill", capacity=64, ram_type="DDR4",
                         speed=3600, msrp=329, ReleaseDate=date(2021, 11, 16))
            ram138 = Ram(ram_name="Corsair Dominator Platinum Extreme", manufacturer="Corsair", capacity=32,
                         ram_type="DDR4", speed=5000, msrp=399, ReleaseDate=date(2021, 12, 7))
            ram139 = Ram(ram_name="Crucial Ballistix MAX Elite", manufacturer="Crucial", capacity=32, ram_type="DDR4",
                         speed=4800, msrp=319, ReleaseDate=date(2021, 11, 9))
            ram140 = Ram(ram_name="Kingston FURY Renegade RGB", manufacturer="Kingston", capacity=32, ram_type="DDR4",
                         speed=4600, msrp=299, ReleaseDate=date(2021, 12, 21))
            ram141 = Ram(ram_name="Team T-Force Night Hawk White", manufacturer="Team Group", capacity=32,
                         ram_type="DDR4", speed=3600, msrp=179, ReleaseDate=date(2021, 12, 14))
            ram142 = Ram(ram_name="Patriot Viper Extreme", manufacturer="Patriot", capacity=32, ram_type="DDR4",
                         speed=4400, msrp=259, ReleaseDate=date(2022, 1, 4))
            ram143 = Ram(ram_name="ADATA XPG LANCER DDR5", manufacturer="ADATA", capacity=32, ram_type="DDR5",
                         speed=5200, msrp=289, ReleaseDate=date(2022, 1, 18))
            ram144 = Ram(ram_name="G.Skill Trident Z5", manufacturer="G.Skill", capacity=32, ram_type="DDR5",
                         speed=5200, msrp=309, ReleaseDate=date(2022, 1, 11))
            ram145 = Ram(ram_name="Corsair Dominator Platinum DDR5", manufacturer="Corsair", capacity=32,
                         ram_type="DDR5", speed=5200, msrp=329, ReleaseDate=date(2022, 2, 1))
            ram146 = Ram(ram_name="Crucial DDR5", manufacturer="Crucial", capacity=32, ram_type="DDR5", speed=4800,
                         msrp=269, ReleaseDate=date(2022, 1, 25))
            ram147 = Ram(ram_name="Kingston FURY Beast DDR5", manufacturer="Kingston", capacity=32, ram_type="DDR5",
                         speed=4800, msrp=259, ReleaseDate=date(2022, 2, 15))
            ram148 = Ram(ram_name="Team T-Force DELTA RGB DDR5", manufacturer="Team Group", capacity=32,
                         ram_type="DDR5", speed=5200, msrp=319, ReleaseDate=date(2022, 3, 1))
            ram149 = Ram(ram_name="GeIL Polaris RGB DDR5", manufacturer="GeIL", capacity=32, ram_type="DDR5",
                         speed=4800, msrp=279, ReleaseDate=date(2022, 2, 8))
            ram150 = Ram(ram_name="Patriot Viper Venom DDR5", manufacturer="Patriot", capacity=32, ram_type="DDR5",
                         speed=5600, msrp=349, ReleaseDate=date(2022, 3, 15))
            ram151 = Ram(ram_name="ADATA XPG LANCER RGB DDR5", manufacturer="ADATA", capacity=32, ram_type="DDR5",
                         speed=6000, msrp=379, ReleaseDate=date(2022, 3, 29))
            ram152 = Ram(ram_name="G.Skill Trident Z5 RGB", manufacturer="G.Skill", capacity=32, ram_type="DDR5",
                         speed=6000, msrp=399, ReleaseDate=date(2022, 3, 8))
            ram153 = Ram(ram_name="Corsair Vengeance DDR5", manufacturer="Corsair", capacity=32, ram_type="DDR5",
                         speed=5200, msrp=289, ReleaseDate=date(2022, 4, 12))
            ram154 = Ram(ram_name="Crucial Ballistix DDR5", manufacturer="Crucial", capacity=32, ram_type="DDR5",
                         speed=5200, msrp=299, ReleaseDate=date(2022, 4, 26))
            ram155 = Ram(ram_name="Kingston FURY Beast RGB DDR5", manufacturer="Kingston", capacity=32, ram_type="DDR5",
                         speed=5600, msrp=339, ReleaseDate=date(2022, 4, 5))
            ram156 = Ram(ram_name="Team T-Force XTREEM DDR5", manufacturer="Team Group", capacity=32, ram_type="DDR5",
                         speed=6400, msrp=429, ReleaseDate=date(2022, 5, 10))
            ram157 = Ram(ram_name="GeIL EVO X DDR5", manufacturer="GeIL", capacity=32, ram_type="DDR5", speed=5600,
                         msrp=349, ReleaseDate=date(2022, 5, 24))
            ram158 = Ram(ram_name="Patriot Venom RGB DDR5", manufacturer="Patriot", capacity=32, ram_type="DDR5",
                         speed=6000, msrp=389, ReleaseDate=date(2022, 5, 3))
            ram159 = Ram(ram_name="ADATA XPG CASTER DDR5", manufacturer="ADATA", capacity=32, ram_type="DDR5",
                         speed=6400, msrp=419, ReleaseDate=date(2022, 6, 7))
            ram160 = Ram(ram_name="G.Skill Trident Z5 RGB Silver", manufacturer="G.Skill", capacity=32, ram_type="DDR5",
                         speed=6400, msrp=429, ReleaseDate=date(2022, 6, 21))
            ram161 = Ram(ram_name="Corsair Dominator Titanium DDR5", manufacturer="Corsair", capacity=32,
                         ram_type="DDR5", speed=6000, msrp=399, ReleaseDate=date(2022, 7, 5))
            ram162 = Ram(ram_name="Crucial Elite DDR5", manufacturer="Crucial", capacity=32, ram_type="DDR5",
                         speed=5600, msrp=349, ReleaseDate=date(2022, 6, 14))
            ram163 = Ram(ram_name="Kingston FURY Renegade DDR5", manufacturer="Kingston", capacity=32, ram_type="DDR5",
                         speed=6400, msrp=419, ReleaseDate=date(2022, 7, 19))
            ram164 = Ram(ram_name="Team T-Force DELTA RGB White DDR5", manufacturer="Team Group", capacity=32,
                         ram_type="DDR5", speed=6000, msrp=389, ReleaseDate=date(2022, 8, 2))
            ram165 = Ram(ram_name="GeIL Polaris White RGB DDR5", manufacturer="GeIL", capacity=32, ram_type="DDR5",
                         speed=5600, msrp=359, ReleaseDate=date(2022, 7, 12))
            ram166 = Ram(ram_name="Patriot Venom RGB White DDR5", manufacturer="Patriot", capacity=32, ram_type="DDR5",
                         speed=6000, msrp=399, ReleaseDate=date(2022, 8, 16))
            ram167 = Ram(ram_name="ADATA XPG LANCER X DDR5", manufacturer="ADATA", capacity=32, ram_type="DDR5",
                         speed=6800, msrp=449, ReleaseDate=date(2022, 8, 30))
            ram168 = Ram(ram_name="G.Skill Trident Z5 Gold DDR5", manufacturer="G.Skill", capacity=32, ram_type="DDR5",
                         speed=6800, msrp=469, ReleaseDate=date(2022, 8, 9))
            ram169 = Ram(ram_name="Corsair Vengeance RGB DDR5", manufacturer="Corsair", capacity=32, ram_type="DDR5",
                         speed=6000, msrp=379, ReleaseDate=date(2022, 9, 13))
            ram170 = Ram(ram_name="Crucial Max DDR5", manufacturer="Crucial", capacity=64, ram_type="DDR5", speed=5600,
                         msrp=529, ReleaseDate=date(2022, 9, 27))
            ram171 = Ram(ram_name="Kingston FURY Renegade White DDR5", manufacturer="Kingston", capacity=32,
                         ram_type="DDR5", speed=6400, msrp=429, ReleaseDate=date(2022, 9, 6))
            ram172 = Ram(ram_name="Team Group DELTA MAX Frost DDR5", manufacturer="Team Group", capacity=32,
                         ram_type="DDR5", speed=6400, msrp=429, ReleaseDate=date(2022, 10, 11))
            ram173 = Ram(ram_name="GeIL Dragon DDR5", manufacturer="GeIL", capacity=32, ram_type="DDR5", speed=6000,
                         msrp=379, ReleaseDate=date(2022, 10, 25))
            ram174 = Ram(ram_name="Patriot Viper Extreme DDR5", manufacturer="Patriot", capacity=32, ram_type="DDR5",
                         speed=6800, msrp=459, ReleaseDate=date(2022, 10, 4))
            ram175 = Ram(ram_name="ADATA XPG SPECTRIX D55G DDR5", manufacturer="ADATA", capacity=32, ram_type="DDR5",
                         speed=6400, msrp=429, ReleaseDate=date(2022, 11, 8))
            ram176 = Ram(ram_name="G.Skill Trident Z5 RGB Matte Black", manufacturer="G.Skill", capacity=32,
                         ram_type="DDR5", speed=7200, msrp=499, ReleaseDate=date(2022, 11, 22))
            ram177 = Ram(ram_name="Corsair Dominator RGB White DDR5", manufacturer="Corsair", capacity=32,
                         ram_type="DDR5", speed=6600, msrp=449, ReleaseDate=date(2022, 11, 1))
            ram178 = Ram(ram_name="Crucial Pro DDR5", manufacturer="Crucial", capacity=32, ram_type="DDR5", speed=6000,
                         msrp=389, ReleaseDate=date(2022, 12, 6))
            ram179 = Ram(ram_name="Kingston FURY Beast Special Edition DDR5", manufacturer="Kingston", capacity=32,
                         ram_type="DDR5", speed=6800, msrp=469, ReleaseDate=date(2022, 12, 20))
            ram180 = Ram(ram_name="Team T-Force Night Hawk DDR5", manufacturer="Team Group", capacity=32,
                         ram_type="DDR5", speed=6400, msrp=429, ReleaseDate=date(2022, 12, 13))
            ram181 = Ram(ram_name="GeIL EVO X III DDR5", manufacturer="GeIL", capacity=32, ram_type="DDR5", speed=6600,
                         msrp=449, ReleaseDate=date(2023, 1, 3))
            ram182 = Ram(ram_name="Patriot Viper Venom Elite DDR5", manufacturer="Patriot", capacity=32,
                         ram_type="DDR5", speed=7200, msrp=499, ReleaseDate=date(2023, 1, 17))
            ram183 = Ram(ram_name="ADATA XPG CASTER RGB DDR5", manufacturer="ADATA", capacity=32, ram_type="DDR5",
                         speed=7200, msrp=499, ReleaseDate=date(2023, 1, 31))
            ram184 = Ram(ram_name="G.Skill Trident Z5 RGB Extreme", manufacturer="G.Skill", capacity=32,
                         ram_type="DDR5", speed=7600, msrp=549, ReleaseDate=date(2023, 1, 10))
            ram185 = Ram(ram_name="Corsair Vengeance Pro DDR5", manufacturer="Corsair", capacity=64, ram_type="DDR5",
                         speed=6000, msrp=529, ReleaseDate=date(2023, 2, 14))
            ram186 = Ram(ram_name="Crucial Elite Pro DDR5", manufacturer="Crucial", capacity=32, ram_type="DDR5",
                         speed=6800, msrp=459, ReleaseDate=date(2023, 2, 28))
            ram187 = Ram(ram_name="Kingston FURY Beast Elite DDR5", manufacturer="Kingston", capacity=32,
                         ram_type="DDR5", speed=7000, msrp=479, ReleaseDate=date(2023, 2, 7))
            ram188 = Ram(ram_name="Team T-Force XTREEM RGB DDR5", manufacturer="Team Group", capacity=32,
                         ram_type="DDR5", speed=7600, msrp=549, ReleaseDate=date(2023, 3, 14))
            ram189 = Ram(ram_name="GeIL Orion Dragon RGB DDR5", manufacturer="GeIL", capacity=32, ram_type="DDR5",
                         speed=6800, msrp=459, ReleaseDate=date(2023, 3, 28))
            ram190 = Ram(ram_name="Patriot Viper Steel RGB DDR5", manufacturer="Patriot", capacity=32, ram_type="DDR5",
                         speed=6800, msrp=459, ReleaseDate=date(2023, 3, 7))
            ram191 = Ram(ram_name="ADATA XPG LANCER RGB Titanium DDR5", manufacturer="ADATA", capacity=32,
                         ram_type="DDR5", speed=7200, msrp=499, ReleaseDate=date(2023, 4, 11))
            ram192 = Ram(ram_name="G.Skill Trident Z5 Royal DDR5", manufacturer="G.Skill", capacity=32, ram_type="DDR5",
                         speed=7600, msrp=569, ReleaseDate=date(2023, 4, 25))
            ram193 = Ram(ram_name="Corsair Dominator Platinum Elite DDR5", manufacturer="Corsair", capacity=32,
                         ram_type="DDR5", speed=7800, msrp=589, ReleaseDate=date(2023, 4, 4))
            ram194 = Ram(ram_name="Crucial Ballistix Pro RGB DDR5", manufacturer="Crucial", capacity=32,
                         ram_type="DDR5", speed=7200, msrp=499, ReleaseDate=date(2023, 5, 9))
            ram195 = Ram(ram_name="Kingston FURY Renegade Extreme DDR5", manufacturer="Kingston", capacity=32,
                         ram_type="DDR5", speed=8000, msrp=599, ReleaseDate=date(2023, 5, 23))
            ram196 = Ram(ram_name="Team T-Force DELTA MAX Crystal DDR5", manufacturer="Team Group", capacity=32,
                         ram_type="DDR5", speed=7200, msrp=499, ReleaseDate=date(2023, 5, 2))
            ram197 = Ram(ram_name="GeIL Dragon Ultimate DDR5", manufacturer="GeIL", capacity=32, ram_type="DDR5",
                         speed=7600, msrp=549, ReleaseDate=date(2023, 6, 6))
            ram198 = Ram(ram_name="Patriot Viper Elite Extreme DDR5", manufacturer="Patriot", capacity=32,
                         ram_type="DDR5", speed=8000, msrp=599, ReleaseDate=date(2023, 6, 20))
            ram199 = Ram(ram_name="ADATA XPG SPECTRIX ZENITH DDR5", manufacturer="ADATA", capacity=32, ram_type="DDR5",
                         speed=8200, msrp=629, ReleaseDate=date(2023, 6, 13))
            ram200 = Ram(ram_name="G.Skill Trident Z5 Royal Elite DDR5", manufacturer="G.Skill", capacity=32,
                         ram_type="DDR5", speed=8200, msrp=649, ReleaseDate=date(2023, 7, 4))
            ram201 = Ram(ram_name="Corsair Vengeance Extreme DDR5", manufacturer="Corsair", capacity=32,
                         ram_type="DDR5", speed=8400, msrp=679, ReleaseDate=date(2023, 7, 18))
            ram202 = Ram(ram_name="Crucial Max Elite DDR5", manufacturer="Crucial", capacity=64, ram_type="DDR5",
                         speed=7600, msrp=749, ReleaseDate=date(2023, 7, 11))
            ram203 = Ram(ram_name="Kingston FURY Beast Special RGB DDR5", manufacturer="Kingston", capacity=32,
                         ram_type="DDR5", speed=8000, msrp=609, ReleaseDate=date(2023, 8, 1))
            ram204 = Ram(ram_name="Team T-Force XTREEM Mirror DDR5", manufacturer="Team Group", capacity=32,
                         ram_type="DDR5", speed=8000, msrp=599, ReleaseDate=date(2023, 8, 15))
            ram205 = Ram(ram_name="GeIL Polaris Crystal DDR5", manufacturer="GeIL", capacity=32, ram_type="DDR5",
                         speed=7800, msrp=589, ReleaseDate=date(2023, 8, 29))
            ram206 = Ram(ram_name="Patriot Venom RGB Ultimate DDR5", manufacturer="Patriot", capacity=32,
                         ram_type="DDR5", speed=8400, msrp=679, ReleaseDate=date(2023, 8, 8))
            ram207 = Ram(ram_name="ADATA GAMMA LEX RGB DDR5", manufacturer="ADATA", capacity=32, ram_type="DDR5",
                         speed=8400, msrp=679, ReleaseDate=date(2023, 9, 12))
            ram208 = Ram(ram_name="G.Skill Trident Z5 RGB Ultimate DDR5", manufacturer="G.Skill", capacity=32,
                         ram_type="DDR5", speed=8600, msrp=699, ReleaseDate=date(2023, 9, 26))
            ram209 = Ram(ram_name="Corsair Dominator Nexus DDR5", manufacturer="Corsair", capacity=32, ram_type="DDR5",
                         speed=8600, msrp=699, ReleaseDate=date(2023, 9, 5))
            ram210 = Ram(ram_name="Crucial Pro Extreme DDR5", manufacturer="Crucial", capacity=32, ram_type="DDR5",
                         speed=8200, msrp=639, ReleaseDate=date(2023, 10, 10))
            ram211 = Ram(ram_name="Kingston FURY Renegade Ultimate DDR5", manufacturer="Kingston", capacity=32,
                         ram_type="DDR5", speed=8600, msrp=699, ReleaseDate=date(2023, 10, 24))
            ram212 = Ram(ram_name="Team T-Force DELTA MAX Ultimate DDR5", manufacturer="Team Group", capacity=32,
                         ram_type="DDR5", speed=8400, msrp=679, ReleaseDate=date(2023, 10, 3))
            ram213 = Ram(ram_name="GeIL Dragon Crystal RGB DDR5", manufacturer="GeIL", capacity=32, ram_type="DDR5",
                         speed=8200, msrp=639, ReleaseDate=date(2023, 11, 7))
            ram214 = Ram(ram_name="Patriot Viper Venom Xtreme DDR5", manufacturer="Patriot", capacity=32,
                         ram_type="DDR5", speed=8800, msrp=729, ReleaseDate=date(2023, 11, 21))
            ram215 = Ram(ram_name="ADATA XPG ZENITH Ultimate DDR5", manufacturer="ADATA", capacity=32, ram_type="DDR5",
                         speed=8800, msrp=729, ReleaseDate=date(2023, 11, 14))
            ram216 = Ram(ram_name="G.Skill Trident Z5 RGB Crystal DDR5", manufacturer="G.Skill", capacity=64,
                         ram_type="DDR5", speed=8000, msrp=899, ReleaseDate=date(2023, 12, 5))
            ram217 = Ram(ram_name="Corsair Dominator Titan DDR5", manufacturer="Corsair", capacity=32, ram_type="DDR5",
                         speed=9000, msrp=799, ReleaseDate=date(2023, 12, 19))
            ram218 = Ram(ram_name="Crucial Ballistix Ultimate DDR5", manufacturer="Crucial", capacity=64,
                         ram_type="DDR5", speed=8400, msrp=949, ReleaseDate=date(2023, 12, 12))
            ram219 = Ram(ram_name="Kingston FURY Beast Ultra DDR5", manufacturer="Kingston", capacity=64,
                         ram_type="DDR5", speed=8400, msrp=949, ReleaseDate=date(2024, 1, 2))
            ram220 = Ram(ram_name="Team T-Force Night Hawk Extreme DDR5", manufacturer="Team Group", capacity=32,
                         ram_type="DDR5", speed=9000, msrp=799, ReleaseDate=date(2024, 1, 16))
            ram221 = Ram(ram_name="GeIL Orion Ultimate DDR5", manufacturer="GeIL", capacity=32, ram_type="DDR5",
                         speed=8800, msrp=749, ReleaseDate=date(2024, 1, 30))
            ram222 = Ram(ram_name="Patriot Viper Supreme DDR5", manufacturer="Patriot", capacity=32, ram_type="DDR5",
                         speed=9200, msrp=829, ReleaseDate=date(2024, 1, 9))
            ram223 = Ram(ram_name="ADATA XPG LANCER Galaxy DDR5", manufacturer="ADATA", capacity=32, ram_type="DDR5",
                         speed=9000, msrp=799, ReleaseDate=date(2024, 2, 13))
            ram224 = Ram(ram_name="G.Skill Trident Z5 Neo DDR5", manufacturer="G.Skill", capacity=32, ram_type="DDR5",
                         speed=9200, msrp=829, ReleaseDate=date(2024, 2, 27))
            ram225 = Ram(ram_name="Corsair Vengeance Ultra RGB DDR5", manufacturer="Corsair", capacity=64,
                         ram_type="DDR5", speed=8800, msrp=999, ReleaseDate=date(2024, 2, 6))
            ram226 = Ram(ram_name="Crucial Pro X-Series DDR5", manufacturer="Crucial", capacity=32, ram_type="DDR5",
                         speed=9000, msrp=799, ReleaseDate=date(2024, 3, 12))
            ram227 = Ram(ram_name="Kingston FURY Renegade Crystal DDR5", manufacturer="Kingston", capacity=32,
                         ram_type="DDR5", speed=9400, msrp=859, ReleaseDate=date(2024, 3, 26))
            ram228 = Ram(ram_name="Team T-Force XTREEM Halo DDR5", manufacturer="Team Group", capacity=32,
                         ram_type="DDR5", speed=9200, msrp=829, ReleaseDate=date(2024, 3, 5))
            ram229 = Ram(ram_name="GeIL EVO X Ultimate RGB DDR5", manufacturer="GeIL", capacity=32, ram_type="DDR5",
                         speed=9000, msrp=799, ReleaseDate=date(2024, 4, 9))
            ram230 = Ram(ram_name="Patriot Viper Ultra RGB DDR5", manufacturer="Patriot", capacity=32, ram_type="DDR5",
                         speed=9400, msrp=859, ReleaseDate=date(2024, 4, 23))
            ram231 = Ram(ram_name="ADATA XPG CASTER Supreme DDR5", manufacturer="ADATA", capacity=32, ram_type="DDR5",
                         speed=9600, msrp=879, ReleaseDate=date(2024, 4, 2))
            ram232 = Ram(ram_name="G.Skill Trident Z5 RGB Quantum DDR5", manufacturer="G.Skill", capacity=64,
                         ram_type="DDR5", speed=9000, msrp=1099, ReleaseDate=date(2024, 5, 7))
            ram233 = Ram(ram_name="Corsair Dominator Elite RGB DDR5", manufacturer="Corsair", capacity=32,
                         ram_type="DDR5", speed=9600, msrp=879, ReleaseDate=date(2024, 5, 21))
            ram234 = Ram(ram_name="Crucial Ballistix Apex DDR5", manufacturer="Crucial", capacity=32, ram_type="DDR5",
                         speed=9400, msrp=859, ReleaseDate=date(2024, 5, 14))
            ram235 = Ram(ram_name="Kingston FURY Beast Apex DDR5", manufacturer="Kingston", capacity=32,
                         ram_type="DDR5", speed=9800, msrp=899, ReleaseDate=date(2024, 6, 4))
            ram236 = Ram(ram_name="Team T-Force DELTA MAX Apex DDR5", manufacturer="Team Group", capacity=32,
                         ram_type="DDR5", speed=9600, msrp=879, ReleaseDate=date(2024, 6, 18))
            ram237 = Ram(ram_name="GeIL Polaris Apex RGB DDR5", manufacturer="GeIL", capacity=32, ram_type="DDR5",
                         speed=9400, msrp=859, ReleaseDate=date(2024, 6, 25))
            ram238 = Ram(ram_name="Patriot Viper Phantom DDR5", manufacturer="Patriot", capacity=32, ram_type="DDR5",
                         speed=9800, msrp=899, ReleaseDate=date(2024, 7, 9))
            ram239 = Ram(ram_name="ADATA XPG SPECTRIX Apex DDR5", manufacturer="ADATA", capacity=32, ram_type="DDR5",
                         speed=10000, msrp=949, ReleaseDate=date(2024, 7, 23))
            ram240 = Ram(ram_name="G.Skill Trident Z5 Royal Apex DDR5", manufacturer="G.Skill", capacity=32,
                         ram_type="DDR5", speed=10000, msrp=949, ReleaseDate=date(2024, 7, 2))
            ram241 = Ram(ram_name="Corsair Vengeance Diamond DDR5", manufacturer="Corsair", capacity=64,
                         ram_type="DDR5", speed=9600, msrp=1199, ReleaseDate=date(2024, 8, 6))
            ram242 = Ram(ram_name="Crucial Elite Diamond DDR5", manufacturer="Crucial", capacity=32, ram_type="DDR5",
                         speed=9800, msrp=919, ReleaseDate=date(2024, 8, 20))
            ram243 = Ram(ram_name="Kingston FURY Renegade Diamond DDR5", manufacturer="Kingston", capacity=32,
                         ram_type="DDR5", speed=10200, msrp=979, ReleaseDate=date(2024, 8, 13))
            ram244 = Ram(ram_name="Team T-Force XTREEM Halo Plus DDR5", manufacturer="Team Group", capacity=32,
                         ram_type="DDR5", speed=10000, msrp=949, ReleaseDate=date(2024, 9, 3))
            ram245 = Ram(ram_name="GeIL Dragon Diamond RGB DDR5", manufacturer="GeIL", capacity=32, ram_type="DDR5",
                         speed=9800, msrp=919, ReleaseDate=date(2024, 9, 17))
            ram246 = Ram(ram_name="Patriot Viper Venom Diamond DDR5", manufacturer="Patriot", capacity=32,
                         ram_type="DDR5", speed=10200, msrp=979, ReleaseDate=date(2024, 9, 10))
            ram247 = Ram(ram_name="ADATA XPG LANCER Diamond DDR5", manufacturer="ADATA", capacity=32, ram_type="DDR5",
                         speed=10400, msrp=999, ReleaseDate=date(2024, 10, 1))
            db.session.add_all([ram1, ram2, ram3, ram4, ram5, ram6, ram7, ram8, ram9, ram10,
                                ram11, ram12, ram13, ram14, ram15, ram16, ram17, ram18, ram19, ram20,
                                ram21, ram22, ram23, ram24, ram25, ram26, ram27, ram28, ram29, ram30,
                                ram31, ram32, ram33, ram34, ram35, ram36, ram37, ram38, ram39, ram40,
                                ram41, ram42, ram43, ram44, ram45, ram46, ram47, ram48, ram49, ram50,
                                ram51, ram52, ram53, ram54, ram55, ram56, ram57, ram58, ram59, ram60,
                                ram61, ram62, ram63, ram64, ram65, ram66, ram67, ram68, ram69, ram70,
                                ram71, ram72, ram73, ram74, ram75, ram76, ram77, ram78, ram79, ram80,
                                ram81, ram82, ram83, ram84, ram85, ram86, ram87, ram88, ram89, ram90,
                                ram91, ram92, ram93, ram94, ram95, ram96, ram97, ram98, ram99, ram100,
                                ram101, ram102, ram103, ram104, ram105, ram106, ram107, ram108, ram109, ram110,
                                ram111, ram112, ram113, ram114, ram115, ram116, ram117, ram118, ram119, ram120,
                                ram121, ram122, ram123, ram124, ram125, ram126, ram127, ram128, ram129, ram130,
                                ram131, ram132, ram133, ram134, ram135, ram136, ram137, ram138, ram139, ram140,
                                ram141, ram142, ram143, ram144, ram145, ram146, ram147, ram148, ram149, ram150,
                                ram151, ram152, ram153, ram154, ram155, ram156, ram157, ram158, ram159, ram160,
                                ram161, ram162, ram163, ram164, ram165, ram166, ram167, ram168, ram169, ram170,
                                ram171, ram172, ram173, ram174, ram175, ram176, ram177, ram178, ram179, ram180,
                                ram181, ram182, ram183, ram184, ram185, ram186, ram187, ram188, ram189, ram190,
                                ram191, ram192, ram193, ram194, ram195, ram196, ram197, ram198, ram199, ram200,
                                ram201, ram202, ram203, ram204, ram205, ram206, ram207, ram208, ram209, ram210,
                                ram211, ram212, ram213, ram214, ram215, ram216, ram217, ram218, ram219, ram220,
                                ram221, ram222, ram223, ram224, ram225, ram226, ram227, ram228, ram229, ram230,
                                ram231, ram232, ram233, ram234, ram235, ram236, ram237, ram238, ram239, ram240,
                                ram241, ram242, ram243, ram244, ram245, ram246, ram247])

        if not Storage.query.first():  # Check if the Storage table is empty
            storage1 = Storage(storage_name="Samsung 970 EVO Plus", manufacturer="Samsung", storage_type="NVMe",
                               capacity="1TB", msrp=250, speed="3500MB/s", ReleaseDate=date(2019, 2, 1))
            storage2 = Storage(storage_name="Samsung 980 Pro", manufacturer="Samsung", storage_type="NVMe",
                               capacity="1TB", msrp=230, speed="7000MB/s", ReleaseDate=date(2020, 9, 22))
            storage3 = Storage(storage_name="Samsung 990 Pro", manufacturer="Samsung", storage_type="NVMe",
                               capacity="2TB", msrp=309, speed="7450MB/s", ReleaseDate=date(2022, 8, 24))
            storage4 = Storage(storage_name="Samsung 980", manufacturer="Samsung", storage_type="NVMe",
                               capacity="500GB", msrp=70, speed="3500MB/s", ReleaseDate=date(2021, 3, 9))
            storage5 = Storage(storage_name="Samsung 990 Evo", manufacturer="Samsung", storage_type="NVMe",
                               capacity="4TB", msrp=500, speed="6000MB/s", ReleaseDate=date(2024, 9, 1))
            storage6 = Storage(storage_name="Samsung 9100 Pro", manufacturer="Samsung", storage_type="NVMe",
                               capacity="8TB", msrp=1300, speed="12000MB/s", ReleaseDate=date(2025, 2, 1))
            storage7 = Storage(storage_name="WD Black SN750", manufacturer="Western Digital", storage_type="NVMe",
                               capacity="250GB", msrp=80, speed="3400MB/s", ReleaseDate=date(2019, 1, 18))
            storage8 = Storage(storage_name="WD Black SN850", manufacturer="Western Digital", storage_type="NVMe",
                               capacity="1TB", msrp=230, speed="7000MB/s", ReleaseDate=date(2020, 10, 8))
            storage9 = Storage(storage_name="WD Black SN850X", manufacturer="Western Digital", storage_type="NVMe",
                               capacity="2TB", msrp=300, speed="7300MB/s", ReleaseDate=date(2022, 8, 1))
            storage10 = Storage(storage_name="WD Black SN770", manufacturer="Western Digital", storage_type="NVMe",
                                capacity="1TB", msrp=130, speed="5150MB/s", ReleaseDate=date(2022, 2, 1))
            storage11 = Storage(storage_name="WD Blue SN550", manufacturer="Western Digital", storage_type="NVMe",
                                capacity="1TB", msrp=100, speed="2400MB/s", ReleaseDate=date(2019, 12, 11))
            storage12 = Storage(storage_name="Crucial P2", manufacturer="Crucial", storage_type="NVMe",
                                capacity="500GB", msrp=65, speed="2300MB/s", ReleaseDate=date(2020, 4, 21))
            storage13 = Storage(storage_name="Crucial P5", manufacturer="Crucial", storage_type="NVMe", capacity="1TB",
                                msrp=180, speed="3400MB/s", ReleaseDate=date(2020, 5, 20))
            storage14 = Storage(storage_name="Crucial P5 Plus", manufacturer="Crucial", storage_type="NVMe",
                                capacity="2TB", msrp=368, speed="6600MB/s", ReleaseDate=date(2021, 8, 3))
            storage15 = Storage(storage_name="Kingston A2000", manufacturer="Kingston", storage_type="NVMe",
                                capacity="500GB", msrp=70, speed="2200MB/s", ReleaseDate=date(2019, 8, 1))
            storage16 = Storage(storage_name="Kingston KC2500", manufacturer="Kingston", storage_type="NVMe",
                                capacity="1TB", msrp=235, speed="3500MB/s", ReleaseDate=date(2020, 5, 20))
            storage17 = Storage(storage_name="Kingston KC3000", manufacturer="Kingston", storage_type="NVMe",
                                capacity="2TB", msrp=400, speed="7000MB/s", ReleaseDate=date(2021, 10, 25))
            storage18 = Storage(storage_name="Kingston NV2", manufacturer="Kingston", storage_type="NVMe",
                                capacity="1TB", msrp=100, speed="3500MB/s", ReleaseDate=date(2022, 9, 1))
            storage19 = Storage(storage_name="SK Hynix Gold P31", manufacturer="SK Hynix", storage_type="NVMe",
                                capacity="1TB", msrp=135, speed="3500MB/s", ReleaseDate=date(2020, 8, 18))
            storage20 = Storage(storage_name="SK Hynix Platinum P41", manufacturer="SK Hynix", storage_type="NVMe",
                                capacity="2TB", msrp=260, speed="7000MB/s", ReleaseDate=date(2022, 5, 30))
            storage21 = Storage(storage_name="Sabrent Rocket Q", manufacturer="Sabrent", storage_type="NVMe",
                                capacity="8TB", msrp=1500, speed="3300MB/s", ReleaseDate=date(2020, 5, 20))
            storage22 = Storage(storage_name="Sabrent Rocket 4.0", manufacturer="Sabrent", storage_type="NVMe",
                                capacity="1TB", msrp=200, speed="5000MB/s", ReleaseDate=date(2019, 8, 1))
            storage23 = Storage(storage_name="Sabrent Rocket 4 Plus", manufacturer="Sabrent", storage_type="NVMe",
                                capacity="2TB", msrp=400, speed="7100MB/s", ReleaseDate=date(2020, 11, 20))
            storage24 = Storage(storage_name="Sabrent Rocket 5", manufacturer="Sabrent", storage_type="NVMe",
                                capacity="2TB", msrp=500, speed="10000MB/s", ReleaseDate=date(2024, 11, 1))
            storage25 = Storage(storage_name="Corsair MP600", manufacturer="Corsair", storage_type="NVMe",
                                capacity="1TB", msrp=200, speed="4950MB/s", ReleaseDate=date(2019, 7, 7))
            storage26 = Storage(storage_name="Corsair MP600 Core", manufacturer="Corsair", storage_type="NVMe",
                                capacity="2TB", msrp=300, speed="4700MB/s", ReleaseDate=date(2021, 1, 1))
            storage27 = Storage(storage_name="Corsair MP600 Pro", manufacturer="Corsair", storage_type="NVMe",
                                capacity="1TB", msrp=225, speed="7000MB/s", ReleaseDate=date(2021, 3, 15))
            storage28 = Storage(storage_name="Seagate FireCuda 520", manufacturer="Seagate", storage_type="NVMe",
                                capacity="1TB", msrp=250, speed="5000MB/s", ReleaseDate=date(2019, 9, 1))
            storage29 = Storage(storage_name="Seagate FireCuda 530", manufacturer="Seagate", storage_type="NVMe",
                                capacity="2TB", msrp=500, speed="7300MB/s", ReleaseDate=date(2021, 7, 19))
            storage30 = Storage(storage_name="Seagate BarraCuda 510", manufacturer="Seagate", storage_type="NVMe",
                                capacity="500GB", msrp=90, speed="3400MB/s", ReleaseDate=date(2019, 7, 1))
            storage31 = Storage(storage_name="Seagate IronWolf 510", manufacturer="Seagate", storage_type="NVMe",
                                capacity="240GB", msrp=70, speed="3150MB/s", ReleaseDate=date(2020, 1, 1))
            storage32 = Storage(storage_name="Intel 665p", manufacturer="Intel", storage_type="NVMe", capacity="1TB",
                                msrp=125, speed="2000MB/s", ReleaseDate=date(2020, 1, 1))
            storage33 = Storage(storage_name="Intel 670p", manufacturer="Intel", storage_type="NVMe", capacity="2TB",
                                msrp=330, speed="2500MB/s", ReleaseDate=date(2021, 2, 1))
            storage34 = Storage(storage_name="Lexar NM610", manufacturer="Lexar", storage_type="NVMe", capacity="250GB",
                                msrp=60, speed="2100MB/s", ReleaseDate=date(2019, 6, 1))
            storage35 = Storage(storage_name="Lexar NM800", manufacturer="Lexar", storage_type="NVMe", capacity="1TB",
                                msrp=170, speed="7400MB/s", ReleaseDate=date(2021, 10, 1))
            storage36 = Storage(storage_name="Patriot Viper VPN100", manufacturer="Patriot", storage_type="NVMe",
                                capacity="512GB", msrp=80, speed="3000MB/s", ReleaseDate=date(2019, 6, 1))
            storage37 = Storage(storage_name="Patriot Viper VP4300", manufacturer="Patriot", storage_type="NVMe",
                                capacity="1TB", msrp=200, speed="7400MB/s", ReleaseDate=date(2021, 6, 1))
            storage38 = Storage(storage_name="PNY XLR8 CS3140", manufacturer="PNY", storage_type="NVMe", capacity="1TB",
                                msrp=230, speed="7500MB/s", ReleaseDate=date(2021, 2, 1))
            storage39 = Storage(storage_name="TeamGroup Cardea Zero Z440", manufacturer="TeamGroup",
                                storage_type="NVMe", capacity="1TB", msrp=200, speed="5000MB/s",
                                ReleaseDate=date(2019, 9, 1))
            storage40 = Storage(storage_name="TeamGroup Cardea A440", manufacturer="TeamGroup", storage_type="NVMe",
                                capacity="2TB", msrp=400, speed="7000MB/s", ReleaseDate=date(2021, 6, 1))
            storage41 = Storage(storage_name="Kioxia Exceria", manufacturer="Kioxia", storage_type="NVMe",
                                capacity="1TB", msrp=120, speed="1700MB/s", ReleaseDate=date(2020, 10, 1))
            storage42 = Storage(storage_name="ADATA XPG SX8200 Pro", manufacturer="ADATA", storage_type="NVMe",
                                capacity="1TB", msrp=180, speed="3500MB/s", ReleaseDate=date(2019, 1, 1))
            storage43 = Storage(storage_name="ADATA XPG Gammix S50", manufacturer="ADATA", storage_type="NVMe",
                                capacity="1TB", msrp=250, speed="5000MB/s", ReleaseDate=date(2019, 9, 1))
            storage44 = Storage(storage_name="ADATA XPG Gammix S70", manufacturer="ADATA", storage_type="NVMe",
                                capacity="2TB", msrp=400, speed="7400MB/s", ReleaseDate=date(2020, 11, 1))
            storage45 = Storage(storage_name="Gigabyte Aorus Gen5 10000", manufacturer="Gigabyte", storage_type="NVMe",
                                capacity="2TB", msrp=340, speed="10000MB/s", ReleaseDate=date(2023, 2, 1))
            storage46 = Storage(storage_name="MSI Spatium M480", manufacturer="MSI", storage_type="NVMe",
                                capacity="2TB", msrp=430, speed="7000MB/s", ReleaseDate=date(2021, 8, 1))
            storage47 = Storage(storage_name="Mushkin Pilot-E", manufacturer="Mushkin", storage_type="NVMe",
                                capacity="1TB", msrp=160, speed="3500MB/s", ReleaseDate=date(2019, 2, 1))
            storage48 = Storage(storage_name="Intel Optane 905P", manufacturer="Intel", storage_type="NVMe",
                                capacity="380GB", msrp=599, speed="2500MB/s", ReleaseDate=date(2019, 1, 8))
            storage49 = Storage(storage_name="Samsung 970 EVO Plus", manufacturer="Samsung", storage_type="NVMe",
                                capacity="500GB", msrp=129, speed="3500MB/s", ReleaseDate=date(2019, 2, 1))
            storage50 = Storage(storage_name="WD Black SN750", manufacturer="Western Digital", storage_type="NVMe",
                                capacity="1TB", msrp=250, speed="3400MB/s", ReleaseDate=date(2019, 1, 18))
            storage51 = Storage(storage_name="WD Black SN850", manufacturer="Western Digital", storage_type="NVMe",
                                capacity="500GB", msrp=150, speed="7000MB/s", ReleaseDate=date(2020, 10, 8))
            storage52 = Storage(storage_name="Crucial P2", manufacturer="Crucial", storage_type="NVMe", capacity="1TB",
                                msrp=95, speed="2400MB/s", ReleaseDate=date(2020, 4, 21))
            storage53 = Storage(storage_name="Crucial P5", manufacturer="Crucial", storage_type="NVMe",
                                capacity="500GB", msrp=85, speed="3400MB/s", ReleaseDate=date(2020, 5, 20))
            storage54 = Storage(storage_name="Kingston A2000", manufacturer="Kingston", storage_type="NVMe",
                                capacity="1TB", msrp=100, speed="2200MB/s", ReleaseDate=date(2019, 8, 1))
            storage55 = Storage(storage_name="Kingston NV1", manufacturer="Kingston", storage_type="NVMe",
                                capacity="2TB", msrp=250, speed="2100MB/s", ReleaseDate=date(2021, 3, 1))
            storage56 = Storage(storage_name="SK Hynix Gold P31", manufacturer="SK Hynix", storage_type="NVMe",
                                capacity="500GB", msrp=75, speed="3500MB/s", ReleaseDate=date(2020, 8, 18))
            storage57 = Storage(storage_name="Sabrent Rocket 4 Plus", manufacturer="Sabrent", storage_type="NVMe",
                                capacity="4TB", msrp=800, speed="7100MB/s", ReleaseDate=date(2021, 11, 15))
            storage58 = Storage(storage_name="Corsair MP600", manufacturer="Corsair", storage_type="NVMe",
                                capacity="2TB", msrp=349, speed="4950MB/s", ReleaseDate=date(2019, 7, 7))
            storage59 = Storage(storage_name="Seagate FireCuda 520", manufacturer="Seagate", storage_type="NVMe",
                                capacity="2TB", msrp=429, speed="5000MB/s", ReleaseDate=date(2019, 9, 1))
            storage60 = Storage(storage_name="Lexar NM620", manufacturer="Lexar", storage_type="NVMe", capacity="1TB",
                                msrp=150, speed="3300MB/s", ReleaseDate=date(2021, 4, 1))
            storage61 = Storage(storage_name="Patriot P300", manufacturer="Patriot", storage_type="NVMe",
                                capacity="1TB", msrp=115, speed="2100MB/s", ReleaseDate=date(2020, 2, 1))
            storage62 = Storage(storage_name="PNY XLR8 CS3030", manufacturer="PNY", storage_type="NVMe",
                                capacity="500GB", msrp=65, speed="3500MB/s", ReleaseDate=date(2019, 1, 1))
            storage63 = Storage(storage_name="TeamGroup MP33", manufacturer="TeamGroup", storage_type="NVMe",
                                capacity="512GB", msrp=60, speed="1700MB/s", ReleaseDate=date(2019, 6, 1))
            storage64 = Storage(storage_name="Crucial T700", manufacturer="Crucial", storage_type="NVMe",
                                capacity="2TB", msrp=340, speed="12000MB/s", ReleaseDate=date(2023, 5, 1))
            storage65 = Storage(storage_name="Silicon Power US70", manufacturer="Silicon Power", storage_type="NVMe",
                                capacity="2TB", msrp=300, speed="5000MB/s", ReleaseDate=date(2020, 7, 1))
            storage66 = Storage(storage_name="Kioxia Exceria Plus", manufacturer="Kioxia", storage_type="NVMe",
                                capacity="1TB", msrp=170, speed="3400MB/s", ReleaseDate=date(2019, 8, 1))
            storage67 = Storage(storage_name="Samsung 870 EVO", manufacturer="Samsung", storage_type="SSD",
                                capacity="1TB", msrp=130, speed="560MB/s", ReleaseDate=date(2021, 1, 20))
            storage68 = Storage(storage_name="Samsung 870 QVO", manufacturer="Samsung", storage_type="SSD",
                                capacity="8TB", msrp=900, speed="560MB/s", ReleaseDate=date(2020, 8, 24))
            storage69 = Storage(storage_name="Samsung 870 QVO", manufacturer="Samsung", storage_type="SSD",
                                capacity="2TB", msrp=250, speed="560MB/s", ReleaseDate=date(2020, 6, 30))
            storage70 = Storage(storage_name="WD Blue 3D NAND", manufacturer="Western Digital", storage_type="SSD",
                                capacity="4TB", msrp=500, speed="560MB/s", ReleaseDate=date(2020, 7, 1))
            storage71 = Storage(storage_name="WD Red SA500", manufacturer="Western Digital", storage_type="SSD",
                                capacity="1TB", msrp=170, speed="560MB/s", ReleaseDate=date(2019, 10, 24))
            storage72 = Storage(storage_name="Crucial MX500", manufacturer="Crucial", storage_type="SSD",
                                capacity="4TB", msrp=500, speed="560MB/s", ReleaseDate=date(2021, 11, 1))
            storage73 = Storage(storage_name="Crucial BX500", manufacturer="Crucial", storage_type="SSD",
                                capacity="2TB", msrp=214, speed="540MB/s", ReleaseDate=date(2019, 10, 30))
            storage74 = Storage(storage_name="Kingston KC600", manufacturer="Kingston", storage_type="SSD",
                                capacity="1TB", msrp=125, speed="550MB/s", ReleaseDate=date(2019, 10, 1))
            storage75 = Storage(storage_name="ADATA Ultimate SU750", manufacturer="ADATA", storage_type="SSD",
                                capacity="1TB", msrp=150, speed="550MB/s", ReleaseDate=date(2019, 2, 19))
            storage76 = Storage(storage_name="ADATA Ultimate SU635", manufacturer="ADATA", storage_type="SSD",
                                capacity="480GB", msrp=60, speed="520MB/s", ReleaseDate=date(2019, 6, 1))
            storage77 = Storage(storage_name="TeamGroup GX2", manufacturer="TeamGroup", storage_type="SSD",
                                capacity="1TB", msrp=100, speed="530MB/s", ReleaseDate=date(2019, 7, 1))
            storage78 = Storage(storage_name="Patriot Burst", manufacturer="Patriot", storage_type="SSD",
                                capacity="480GB", msrp=45, speed="560MB/s", ReleaseDate=date(2019, 1, 15))
            storage79 = Storage(storage_name="Patriot P200", manufacturer="Patriot", storage_type="SSD",
                                capacity="512GB", msrp=55, speed="530MB/s", ReleaseDate=date(2019, 6, 1))
            storage80 = Storage(storage_name="PNY CS900", manufacturer="PNY", storage_type="SSD", capacity="1TB",
                                msrp=100, speed="535MB/s", ReleaseDate=date(2019, 3, 1))
            storage81 = Storage(storage_name="Seagate BarraCuda SSD", manufacturer="Seagate", storage_type="SSD",
                                capacity="1TB", msrp=130, speed="560MB/s", ReleaseDate=date(2019, 7, 1))
            storage82 = Storage(storage_name="Seagate IronWolf 110", manufacturer="Seagate", storage_type="SSD",
                                capacity="480GB", msrp=130, speed="560MB/s", ReleaseDate=date(2019, 1, 22))
            storage83 = Storage(storage_name="Seagate FireCuda 120", manufacturer="Seagate", storage_type="SSD",
                                capacity="2TB", msrp=460, speed="560MB/s", ReleaseDate=date(2020, 5, 15))
            storage84 = Storage(storage_name="Mushkin Source", manufacturer="Mushkin", storage_type="SSD",
                                capacity="1TB", msrp=110, speed="560MB/s", ReleaseDate=date(2019, 5, 1))
            storage85 = Storage(storage_name="Silicon Power A55", manufacturer="Silicon Power", storage_type="SSD",
                                capacity="1TB", msrp=90, speed="500MB/s", ReleaseDate=date(2019, 4, 1))
            storage86 = Storage(storage_name="SK Hynix Gold S31", manufacturer="SK Hynix", storage_type="SSD",
                                capacity="1TB", msrp=124, speed="560MB/s", ReleaseDate=date(2019, 8, 18))
            storage87 = Storage(storage_name="Lexar NS100", manufacturer="Lexar", storage_type="SSD", capacity="512GB",
                                msrp=60, speed="550MB/s", ReleaseDate=date(2019, 4, 1))
            storage88 = Storage(storage_name="Samsung 870 EVO", manufacturer="Samsung", storage_type="SSD",
                                capacity="4TB", msrp=480, speed="560MB/s", ReleaseDate=date(2021, 1, 20))
            storage89 = Storage(storage_name="Samsung 870 EVO", manufacturer="Samsung", storage_type="SSD",
                                capacity="500GB", msrp=60, speed="560MB/s", ReleaseDate=date(2021, 1, 20))
            storage90 = Storage(storage_name="Samsung 870 QVO", manufacturer="Samsung", storage_type="SSD",
                                capacity="4TB", msrp=500, speed="560MB/s", ReleaseDate=date(2020, 6, 30))
            storage91 = Storage(storage_name="Samsung 870 QVO", manufacturer="Samsung", storage_type="SSD",
                                capacity="1TB", msrp=130, speed="560MB/s", ReleaseDate=date(2020, 6, 30))
            storage92 = Storage(storage_name="WD Red SA500", manufacturer="Western Digital", storage_type="SSD",
                                capacity="4TB", msrp=600, speed="560MB/s", ReleaseDate=date(2019, 10, 24))
            storage93 = Storage(storage_name="WD Red SA500", manufacturer="Western Digital", storage_type="SSD",
                                capacity="500GB", msrp=75, speed="560MB/s", ReleaseDate=date(2019, 10, 24))
            storage94 = Storage(storage_name="Crucial MX500", manufacturer="Crucial", storage_type="SSD",
                                capacity="1TB", msrp=130, speed="560MB/s", ReleaseDate=date(2021, 7, 1))
            storage95 = Storage(storage_name="Crucial BX500", manufacturer="Crucial", storage_type="SSD",
                                capacity="480GB", msrp=60, speed="540MB/s", ReleaseDate=date(2019, 8, 1))
            storage96 = Storage(storage_name="Kingston KC600", manufacturer="Kingston", storage_type="SSD",
                                capacity="512GB", msrp=70, speed="550MB/s", ReleaseDate=date(2019, 10, 1))
            storage97 = Storage(storage_name="SK Hynix Gold S31", manufacturer="SK Hynix", storage_type="SSD",
                                capacity="500GB", msrp=78, speed="560MB/s", ReleaseDate=date(2019, 8, 18))
            storage98 = Storage(storage_name="TeamGroup GX2", manufacturer="TeamGroup", storage_type="SSD",
                                capacity="512GB", msrp=50, speed="530MB/s", ReleaseDate=date(2019, 7, 1))
            storage99 = Storage(storage_name="Patriot Burst", manufacturer="Patriot", storage_type="SSD",
                                capacity="960GB", msrp=90, speed="560MB/s", ReleaseDate=date(2019, 9, 1))
            storage100 = Storage(storage_name="PNY CS900", manufacturer="PNY", storage_type="SSD", capacity="240GB",
                                 msrp=35, speed="515MB/s", ReleaseDate=date(2019, 3, 1))
            storage101 = Storage(storage_name="Kioxia Exceria SATA", manufacturer="Kioxia", storage_type="SSD",
                                 capacity="960GB", msrp=100, speed="555MB/s", ReleaseDate=date(2020, 9, 1))
            storage102 = Storage(storage_name="Kioxia Exceria SATA", manufacturer="Kioxia", storage_type="SSD",
                                 capacity="480GB", msrp=50, speed="555MB/s", ReleaseDate=date(2020, 9, 1))
            storage103 = Storage(storage_name="Micron 5210 ION", manufacturer="Micron", storage_type="SSD",
                                 capacity="7.68TB", msrp=1000, speed="540MB/s", ReleaseDate=date(2019, 6, 1))
            storage104 = Storage(storage_name="Crucial MX500", manufacturer="Crucial", storage_type="SSD",
                                 capacity="500GB", msrp=70, speed="560MB/s", ReleaseDate=date(2021, 7, 1))
            storage105 = Storage(storage_name="Crucial BX500", manufacturer="Crucial", storage_type="SSD",
                                 capacity="120GB", msrp=25, speed="540MB/s", ReleaseDate=date(2019, 1, 1))
            storage106 = Storage(storage_name="Patriot P200", manufacturer="Patriot", storage_type="SSD",
                                 capacity="1TB", msrp=100, speed="530MB/s", ReleaseDate=date(2019, 6, 1))
            storage107 = Storage(storage_name="PNY CS900", manufacturer="PNY", storage_type="SSD", capacity="480GB",
                                 msrp=55, speed="515MB/s", ReleaseDate=date(2019, 3, 1))
            storage108 = Storage(storage_name="Mushkin Source", manufacturer="Mushkin", storage_type="SSD",
                                 capacity="120GB", msrp=25, speed="560MB/s", ReleaseDate=date(2019, 5, 1))
            storage109 = Storage(storage_name="WD Blue 3D NAND", manufacturer="Western Digital", storage_type="SSD",
                                 capacity="2TB", msrp=250, speed="560MB/s", ReleaseDate=date(2019, 5, 1))
            storage110 = Storage(storage_name="Kingston DC500R", manufacturer="Kingston", storage_type="SSD",
                                 capacity="3.84TB", msrp=800, speed="555MB/s", ReleaseDate=date(2019, 4, 1))
            storage111 = Storage(storage_name="WD Blue", manufacturer="Western Digital", storage_type="HDD",
                                 capacity="1TB", msrp=50, speed="7200RPM", ReleaseDate=date(2019, 1, 1))
            storage112 = Storage(storage_name="WD Blue", manufacturer="Western Digital", storage_type="HDD",
                                 capacity="4TB", msrp=100, speed="5400RPM", ReleaseDate=date(2019, 6, 1))
            storage113 = Storage(storage_name="WD Blue", manufacturer="Western Digital", storage_type="HDD",
                                 capacity="6TB", msrp=140, speed="5400RPM", ReleaseDate=date(2019, 6, 1))
            storage114 = Storage(storage_name="WD Blue", manufacturer="Western Digital", storage_type="HDD",
                                 capacity="8TB", msrp=180, speed="5400RPM", ReleaseDate=date(2020, 6, 1))
            storage115 = Storage(storage_name="WD Black", manufacturer="Western Digital", storage_type="HDD",
                                 capacity="2TB", msrp=120, speed="7200RPM", ReleaseDate=date(2019, 5, 1))
            storage116 = Storage(storage_name="WD Black", manufacturer="Western Digital", storage_type="HDD",
                                 capacity="6TB", msrp=250, speed="7200RPM", ReleaseDate=date(2019, 5, 1))
            storage117 = Storage(storage_name="WD Black", manufacturer="Western Digital", storage_type="HDD",
                                 capacity="8TB", msrp=300, speed="7200RPM", ReleaseDate=date(2020, 8, 1))
            storage118 = Storage(storage_name="WD Red Plus", manufacturer="Western Digital", storage_type="HDD",
                                 capacity="4TB", msrp=120, speed="5400RPM", ReleaseDate=date(2021, 7, 1))
            storage119 = Storage(storage_name="WD Red Plus", manufacturer="Western Digital", storage_type="HDD",
                                 capacity="8TB", msrp=200, speed="5400RPM", ReleaseDate=date(2021, 7, 1))
            storage120 = Storage(storage_name="WD Red Pro", manufacturer="Western Digital", storage_type="HDD",
                                 capacity="14TB", msrp=450, speed="7200RPM", ReleaseDate=date(2019, 10, 1))
            storage121 = Storage(storage_name="WD Red Pro", manufacturer="Western Digital", storage_type="HDD",
                                 capacity="18TB", msrp=600, speed="7200RPM", ReleaseDate=date(2020, 9, 1))
            storage122 = Storage(storage_name="WD Red Pro", manufacturer="Western Digital", storage_type="HDD",
                                 capacity="22TB", msrp=600, speed="7200RPM", ReleaseDate=date(2022, 7, 1))
            storage123 = Storage(storage_name="WD Purple", manufacturer="Western Digital", storage_type="HDD",
                                 capacity="6TB", msrp=150, speed="5400RPM", ReleaseDate=date(2019, 5, 1))
            storage124 = Storage(storage_name="WD Purple", manufacturer="Western Digital", storage_type="HDD",
                                 capacity="12TB", msrp=300, speed="5400RPM", ReleaseDate=date(2019, 10, 1))
            storage125 = Storage(storage_name="WD Purple", manufacturer="Western Digital", storage_type="HDD",
                                 capacity="18TB", msrp=500, speed="5400RPM", ReleaseDate=date(2020, 10, 1))
            storage126 = Storage(storage_name="WD Purple Pro", manufacturer="Western Digital", storage_type="HDD",
                                 capacity="18TB", msrp=550, speed="7200RPM", ReleaseDate=date(2021, 9, 1))
            storage127 = Storage(storage_name="WD Gold", manufacturer="Western Digital", storage_type="HDD",
                                 capacity="16TB", msrp=520, speed="7200RPM", ReleaseDate=date(2019, 7, 1))
            storage128 = Storage(storage_name="WD Gold", manufacturer="Western Digital", storage_type="HDD",
                                 capacity="18TB", msrp=600, speed="7200RPM", ReleaseDate=date(2020, 7, 1))
            storage129 = Storage(storage_name="WD Gold", manufacturer="Western Digital", storage_type="HDD",
                                 capacity="20TB", msrp=650, speed="7200RPM", ReleaseDate=date(2021, 11, 1))
            storage130 = Storage(storage_name="WD Gold", manufacturer="Western Digital", storage_type="HDD",
                                 capacity="22TB", msrp=700, speed="7200RPM", ReleaseDate=date(2022, 7, 1))
            storage131 = Storage(storage_name="WD Ultrastar DC HC550", manufacturer="Western Digital",
                                 storage_type="HDD", capacity="18TB", msrp=600, speed="7200RPM",
                                 ReleaseDate=date(2019, 12, 1))
            storage132 = Storage(storage_name="WD Blue Mobile", manufacturer="Western Digital", storage_type="HDD",
                                 capacity="2TB", msrp=80, speed="5400RPM", ReleaseDate=date(2019, 3, 1))
            storage133 = Storage(storage_name="Seagate BarraCuda", manufacturer="Seagate", storage_type="HDD",
                                 capacity="2TB", msrp=60, speed="7200RPM", ReleaseDate=date(2019, 4, 1))
            storage134 = Storage(storage_name="Seagate BarraCuda", manufacturer="Seagate", storage_type="HDD",
                                 capacity="4TB", msrp=100, speed="5400RPM", ReleaseDate=date(2019, 4, 1))
            storage135 = Storage(storage_name="Seagate BarraCuda", manufacturer="Seagate", storage_type="HDD",
                                 capacity="8TB", msrp=180, speed="5400RPM", ReleaseDate=date(2019, 9, 1))
            storage136 = Storage(storage_name="Seagate BarraCuda Pro", manufacturer="Seagate", storage_type="HDD",
                                 capacity="14TB", msrp=500, speed="7200RPM", ReleaseDate=date(2019, 7, 1))
            storage137 = Storage(storage_name="Seagate IronWolf", manufacturer="Seagate", storage_type="HDD",
                                 capacity="8TB", msrp=220, speed="7200RPM", ReleaseDate=date(2019, 1, 1))
            storage138 = Storage(storage_name="Seagate IronWolf", manufacturer="Seagate", storage_type="HDD",
                                 capacity="16TB", msrp=580, speed="7200RPM", ReleaseDate=date(2019, 6, 4))
            storage139 = Storage(storage_name="Seagate IronWolf Pro", manufacturer="Seagate", storage_type="HDD",
                                 capacity="16TB", msrp=630, speed="7200RPM", ReleaseDate=date(2019, 6, 4))
            storage140 = Storage(storage_name="Seagate IronWolf Pro", manufacturer="Seagate", storage_type="HDD",
                                 capacity="20TB", msrp=650, speed="7200RPM", ReleaseDate=date(2022, 9, 1))
            storage141 = Storage(storage_name="Seagate SkyHawk", manufacturer="Seagate", storage_type="HDD",
                                 capacity="10TB", msrp=300, speed="5400RPM", ReleaseDate=date(2019, 3, 1))
            storage142 = Storage(storage_name="Seagate SkyHawk AI", manufacturer="Seagate", storage_type="HDD",
                                 capacity="18TB", msrp=520, speed="5400RPM", ReleaseDate=date(2020, 10, 1))
            storage143 = Storage(storage_name="Seagate Exos X16", manufacturer="Seagate", storage_type="HDD",
                                 capacity="16TB", msrp=600, speed="7200RPM", ReleaseDate=date(2019, 6, 4))
            storage144 = Storage(storage_name="Seagate Exos X18", manufacturer="Seagate", storage_type="HDD",
                                 capacity="18TB", msrp=650, speed="7200RPM", ReleaseDate=date(2020, 9, 1))
            storage145 = Storage(storage_name="Seagate Exos X20", manufacturer="Seagate", storage_type="HDD",
                                 capacity="20TB", msrp=700, speed="7200RPM", ReleaseDate=date(2021, 12, 1))
            storage146 = Storage(storage_name="Toshiba P300", manufacturer="Toshiba", storage_type="HDD",
                                 capacity="3TB", msrp=90, speed="7200RPM", ReleaseDate=date(2019, 2, 1))
            storage147 = Storage(storage_name="Toshiba P300", manufacturer="Toshiba", storage_type="HDD",
                                 capacity="6TB", msrp=180, speed="5400RPM", ReleaseDate=date(2021, 2, 1))
            storage148 = Storage(storage_name="Toshiba X300", manufacturer="Toshiba", storage_type="HDD",
                                 capacity="8TB", msrp=240, speed="7200RPM", ReleaseDate=date(2019, 4, 1))
            storage149 = Storage(storage_name="Toshiba X300", manufacturer="Toshiba", storage_type="HDD",
                                 capacity="14TB", msrp=500, speed="7200RPM", ReleaseDate=date(2020, 8, 1))
            storage150 = Storage(storage_name="Toshiba N300", manufacturer="Toshiba", storage_type="HDD",
                                 capacity="14TB", msrp=480, speed="7200RPM", ReleaseDate=date(2019, 12, 1))
            storage151 = Storage(storage_name="Toshiba N300", manufacturer="Toshiba", storage_type="HDD",
                                 capacity="18TB", msrp=600, speed="7200RPM", ReleaseDate=date(2021, 8, 1))
            storage152 = Storage(storage_name="Toshiba L200", manufacturer="Toshiba", storage_type="HDD",
                                 capacity="2TB", msrp=80, speed="5400RPM", ReleaseDate=date(2019, 5, 1))
            storage153 = Storage(storage_name="Toshiba L200", manufacturer="Toshiba", storage_type="HDD",
                                 capacity="1TB", msrp=50, speed="5400RPM", ReleaseDate=date(2019, 5, 1))
            storage154 = Storage(storage_name="HGST Ultrastar He12", manufacturer="HGST", storage_type="HDD",
                                 capacity="12TB", msrp=400, speed="7200RPM", ReleaseDate=date(2019, 1, 1))
            storage155 = Storage(storage_name="HGST Ultrastar DC HC650", manufacturer="HGST", storage_type="HDD",
                                 capacity="20TB", msrp=800, speed="7200RPM", ReleaseDate=date(2020, 12, 1))
            storage156 = Storage(storage_name="Seagate IronWolf", manufacturer="Seagate", storage_type="HDD",
                                 capacity="4TB", msrp=140, speed="5900RPM", ReleaseDate=date(2019, 1, 1))
            storage157 = Storage(storage_name="Seagate IronWolf Pro", manufacturer="Seagate", storage_type="HDD",
                                 capacity="8TB", msrp=280, speed="7200RPM", ReleaseDate=date(2019, 1, 1))
            storage158 = Storage(storage_name="Seagate SkyHawk", manufacturer="Seagate", storage_type="HDD",
                                 capacity="18TB", msrp=500, speed="5400RPM", ReleaseDate=date(2021, 10, 1))
            storage159 = Storage(storage_name="Toshiba MG08", manufacturer="Toshiba", storage_type="HDD",
                                 capacity="16TB", msrp=520, speed="7200RPM", ReleaseDate=date(2019, 1, 1))
            storage160 = Storage(storage_name="Toshiba MG10", manufacturer="Toshiba", storage_type="HDD",
                                 capacity="20TB", msrp=650, speed="7200RPM", ReleaseDate=date(2021, 9, 1))
            storage161 = Storage(storage_name="WD Red Plus", manufacturer="Western Digital", storage_type="HDD",
                                 capacity="6TB", msrp=150, speed="5400RPM", ReleaseDate=date(2021, 7, 1))
            storage162 = Storage(storage_name="WD Purple", manufacturer="Western Digital", storage_type="HDD",
                                 capacity="8TB", msrp=200, speed="5400RPM", ReleaseDate=date(2019, 3, 1))
            storage163 = Storage(storage_name="Seagate SkyHawk", manufacturer="Seagate", storage_type="HDD",
                                 capacity="8TB", msrp=180, speed="5400RPM", ReleaseDate=date(2019, 3, 1))
            storage164 = Storage(storage_name="Toshiba X300", manufacturer="Toshiba", storage_type="HDD",
                                 capacity="16TB", msrp=520, speed="7200RPM", ReleaseDate=date(2021, 6, 1))
            storage165 = Storage(storage_name="Toshiba P300", manufacturer="Toshiba", storage_type="HDD",
                                 capacity="1TB", msrp=45, speed="7200RPM", ReleaseDate=date(2019, 2, 1))
            storage166 = Storage(storage_name="Seagate FireCuda SSHD", manufacturer="Seagate", storage_type="HDD",
                                 capacity="2TB", msrp=100, speed="5400RPM", ReleaseDate=date(2019, 1, 1))
            storage167 = Storage(storage_name="WD Red Plus", manufacturer="Western Digital", storage_type="HDD",
                                 capacity="2TB", msrp=80, speed="5400RPM", ReleaseDate=date(2021, 7, 1))
            storage168 = Storage(storage_name="WD Purple", manufacturer="Western Digital", storage_type="HDD",
                                 capacity="4TB", msrp=100, speed="5400RPM", ReleaseDate=date(2019, 3, 1))
            storage169 = Storage(storage_name="WD Purple Pro", manufacturer="Western Digital", storage_type="HDD",
                                 capacity="8TB", msrp=300, speed="7200RPM", ReleaseDate=date(2021, 9, 1))
            storage170 = Storage(storage_name="WD Black", manufacturer="Western Digital", storage_type="HDD",
                                 capacity="4TB", msrp=200, speed="7200RPM", ReleaseDate=date(2019, 5, 1))
            storage171 = Storage(storage_name="Seagate BarraCuda", manufacturer="Seagate", storage_type="HDD",
                                 capacity="1TB", msrp=45, speed="7200RPM", ReleaseDate=date(2019, 4, 1))
            storage172 = Storage(storage_name="Seagate BarraCuda", manufacturer="Seagate", storage_type="HDD",
                                 capacity="6TB", msrp=150, speed="5400RPM", ReleaseDate=date(2019, 9, 1))
            storage173 = Storage(storage_name="Seagate SkyHawk", manufacturer="Seagate", storage_type="HDD",
                                 capacity="4TB", msrp=90, speed="5400RPM", ReleaseDate=date(2019, 3, 1))
            storage174 = Storage(storage_name="Seagate Exos 2X14", manufacturer="Seagate", storage_type="HDD",
                                 capacity="14TB", msrp=600, speed="7200RPM", ReleaseDate=date(2021, 6, 1))
            storage175 = Storage(storage_name="Toshiba X300", manufacturer="Toshiba", storage_type="HDD",
                                 capacity="4TB", msrp=150, speed="7200RPM", ReleaseDate=date(2019, 4, 1))
            storage176 = Storage(storage_name="Toshiba N300", manufacturer="Toshiba", storage_type="HDD",
                                 capacity="8TB", msrp=250, speed="7200RPM", ReleaseDate=date(2019, 1, 1))
            storage177 = Storage(storage_name="Toshiba L200", manufacturer="Toshiba", storage_type="HDD",
                                 capacity="500GB", msrp=40, speed="5400RPM", ReleaseDate=date(2019, 5, 1))
            storage178 = Storage(storage_name="Seagate IronWolf", manufacturer="Seagate", storage_type="HDD",
                                 capacity="4TB", msrp=140, speed="5900RPM", ReleaseDate=date(2019, 1, 1))
            storage179 = Storage(storage_name="Seagate IronWolf Pro", manufacturer="Seagate", storage_type="HDD",
                                 capacity="8TB", msrp=280, speed="7200RPM", ReleaseDate=date(2019, 1, 1))
            storage180 = Storage(storage_name="Seagate SkyHawk", manufacturer="Seagate", storage_type="HDD",
                                 capacity="18TB", msrp=500, speed="5400RPM", ReleaseDate=date(2021, 10, 1))
            storage181 = Storage(storage_name="Toshiba MG08", manufacturer="Toshiba", storage_type="HDD",
                                 capacity="16TB", msrp=520, speed="7200RPM", ReleaseDate=date(2019, 1, 1))
            storage182 = Storage(storage_name="Toshiba MG10", manufacturer="Toshiba", storage_type="HDD",
                                 capacity="20TB", msrp=650, speed="7200RPM", ReleaseDate=date(2021, 9, 1))
            storage183 = Storage(storage_name="WD Red Plus", manufacturer="Western Digital", storage_type="HDD",
                                 capacity="6TB", msrp=150, speed="5400RPM", ReleaseDate=date(2021, 7, 1))
            storage184 = Storage(storage_name="WD Purple", manufacturer="Western Digital", storage_type="HDD",
                                 capacity="8TB", msrp=200, speed="5400RPM", ReleaseDate=date(2019, 3, 1))
            storage185 = Storage(storage_name="Seagate SkyHawk", manufacturer="Seagate", storage_type="HDD",
                                 capacity="8TB", msrp=180, speed="5400RPM", ReleaseDate=date(2019, 3, 1))
            storage186 = Storage(storage_name="Toshiba X300", manufacturer="Toshiba", storage_type="HDD",
                                 capacity="16TB", msrp=520, speed="7200RPM", ReleaseDate=date(2021, 6, 1))
            storage187 = Storage(storage_name="Toshiba P300", manufacturer="Toshiba", storage_type="HDD",
                                 capacity="1TB", msrp=45, speed="7200RPM", ReleaseDate=date(2019, 2, 1))
            storage188 = Storage(storage_name="Seagate FireCuda SSHD", manufacturer="Seagate", storage_type="HDD",
                                 capacity="2TB", msrp=100, speed="5400RPM", ReleaseDate=date(2019, 1, 1))
            storage189 = Storage(storage_name="WD Red Plus", manufacturer="Western Digital", storage_type="HDD",
                                 capacity="2TB", msrp=80, speed="5400RPM", ReleaseDate=date(2021, 7, 1))
            storage190 = Storage(storage_name="WD Purple", manufacturer="Western Digital", storage_type="HDD",
                                 capacity="4TB", msrp=100, speed="5400RPM", ReleaseDate=date(2019, 3, 1))
            storage191 = Storage(storage_name="WD Purple Pro", manufacturer="Western Digital", storage_type="HDD",
                                 capacity="8TB", msrp=300, speed="7200RPM", ReleaseDate=date(2021, 9, 1))
            storage192 = Storage(storage_name="WD Black", manufacturer="Western Digital", storage_type="HDD",
                                 capacity="4TB", msrp=200, speed="7200RPM", ReleaseDate=date(2019, 5, 1))
            storage193 = Storage(storage_name="Seagate BarraCuda", manufacturer="Seagate", storage_type="HDD",
                                 capacity="1TB", msrp=45, speed="7200RPM", ReleaseDate=date(2019, 4, 1))
            storage194 = Storage(storage_name="Seagate BarraCuda", manufacturer="Seagate", storage_type="HDD",
                                 capacity="6TB", msrp=150, speed="5400RPM", ReleaseDate=date(2019, 9, 1))
            storage195 = Storage(storage_name="Seagate SkyHawk", manufacturer="Seagate", storage_type="HDD",
                                 capacity="4TB", msrp=90, speed="5400RPM", ReleaseDate=date(2019, 3, 1))
            storage196 = Storage(storage_name="Seagate Exos 2X14", manufacturer="Seagate", storage_type="HDD",
                                 capacity="14TB", msrp=600, speed="7200RPM", ReleaseDate=date(2021, 6, 1))
            storage197 = Storage(storage_name="Toshiba X300", manufacturer="Toshiba", storage_type="HDD",
                                 capacity="4TB", msrp=150, speed="7200RPM", ReleaseDate=date(2019, 4, 1))
            storage198 = Storage(storage_name="Toshiba N300", manufacturer="Toshiba", storage_type="HDD",
                                 capacity="8TB", msrp=250, speed="7200RPM", ReleaseDate=date(2019, 1, 1))
            storage199 = Storage(storage_name="Toshiba L200", manufacturer="Toshiba", storage_type="HDD",
                                 capacity="500GB", msrp=40, speed="5400RPM", ReleaseDate=date(2019, 5, 1))
            storage200 = Storage(storage_name="Toshiba P300", manufacturer="Toshiba", storage_type="HDD",
                                 capacity="1TB", msrp=45, speed="7200RPM", ReleaseDate=date(2019, 2, 1))

            db.session.add_all(
                [storage1, storage2, storage3, storage4, storage5, storage6, storage7, storage8, storage9, storage10,
                 storage11, storage12, storage13, storage14, storage15, storage16, storage17, storage18, storage19,
                 storage20, storage21, storage22, storage23, storage24, storage25, storage26, storage27, storage28,
                 storage29, storage30, storage31, storage32, storage33, storage34, storage35, storage36, storage37,
                 storage38, storage39, storage40, storage41, storage42, storage43, storage44, storage45, storage46,
                 storage47, storage48, storage49, storage50, storage51, storage52, storage53, storage54, storage55,
                 storage56, storage57, storage58, storage59, storage60, storage61, storage62, storage63, storage64,
                 storage65, storage66, storage67, storage68, storage69, storage70, storage71, storage72, storage73,
                 storage74, storage75, storage76, storage77, storage78, storage79, storage80, storage81, storage82,
                 storage83, storage84, storage85, storage86, storage87, storage88, storage89, storage90, storage91,
                 storage92, storage93, storage94, storage95, storage96, storage97, storage98, storage99, storage100,
                 storage101, storage102, storage103, storage104, storage105, storage106, storage107, storage108,
                 storage109, storage110, storage111, storage112, storage113, storage114, storage115, storage116,
                 storage117, storage118, storage119, storage120, storage121, storage122, storage123, storage124,
                 storage125, storage126, storage127, storage128, storage129, storage130, storage131, storage132,
                 storage133, storage134, storage135, storage136, storage137, storage138, storage139, storage140,
                 storage141, storage142, storage143, storage144, storage145, storage146, storage147, storage148,
                 storage149, storage150, storage151, storage152, storage153, storage154, storage155, storage156,
                 storage157, storage158, storage159, storage160, storage161, storage162, storage163, storage164,
                 storage165, storage166, storage167, storage168, storage169, storage170, storage171, storage172,
                 storage173, storage174, storage175, storage176, storage177, storage178, storage179, storage180,
                 storage181, storage182, storage183, storage184, storage185, storage186, storage187, storage188,
                 storage189, storage190, storage191, storage192, storage193, storage194, storage195, storage196,
                 storage197, storage198, storage199, storage200])

        if not Psu.query.first():  # Check if the Psu table is empty
            # Corsair PSUs
            psu1 = Psu(psu_name="Corsair RM550x", manufacturer="Corsair", wattage=550, efficiency_rating="80+ Gold",
                       modular="Fully", msrp=109, ReleaseDate=date(2021, 6, 1))
            psu2 = Psu(psu_name="Corsair RM650x", manufacturer="Corsair", wattage=650, efficiency_rating="80+ Gold",
                       modular="Fully", msrp=119, ReleaseDate=date(2021, 6, 1))
            psu3 = Psu(psu_name="Corsair RM750x", manufacturer="Corsair", wattage=750, efficiency_rating="80+ Gold",
                       modular="Fully", msrp=129, ReleaseDate=date(2020, 5, 1))
            psu4 = Psu(psu_name="Corsair RM850x", manufacturer="Corsair", wattage=850, efficiency_rating="80+ Gold",
                       modular="Fully", msrp=149, ReleaseDate=date(2020, 5, 1))
            psu5 = Psu(psu_name="Corsair AX850", manufacturer="Corsair", wattage=850, efficiency_rating="80+ Titanium",
                       modular="Fully", msrp=249, ReleaseDate=date(2019, 1, 15))
            psu6 = Psu(psu_name="Corsair AX1000", manufacturer="Corsair", wattage=1000,
                       efficiency_rating="80+ Titanium", modular="Fully", msrp=279, ReleaseDate=date(2019, 1, 15))
            psu7 = Psu(psu_name="Corsair CX550M", manufacturer="Corsair", wattage=550, efficiency_rating="80+ Bronze",
                       modular="Semi", msrp=65, ReleaseDate=date(2019, 3, 1))
            psu8 = Psu(psu_name="Corsair CX650M", manufacturer="Corsair", wattage=650, efficiency_rating="80+ Bronze",
                       modular="Semi", msrp=75, ReleaseDate=date(2019, 3, 1))
            psu9 = Psu(psu_name="Corsair CX750M", manufacturer="Corsair", wattage=750, efficiency_rating="80+ Bronze",
                       modular="Semi", msrp=85, ReleaseDate=date(2019, 3, 1))
            psu10 = Psu(psu_name="Corsair CV550", manufacturer="Corsair", wattage=550, efficiency_rating="80+ Bronze",
                        modular="No", msrp=60, ReleaseDate=date(2020, 2, 1))
            psu11 = Psu(psu_name="Corsair CV650", manufacturer="Corsair", wattage=650, efficiency_rating="80+ Bronze",
                        modular="No", msrp=70, ReleaseDate=date(2020, 2, 1))
            psu12 = Psu(psu_name="Corsair SF750 Platinum", manufacturer="Corsair", wattage=750,
                        efficiency_rating="80+ Platinum", modular="Fully", msrp=179, ReleaseDate=date(2019, 1, 7))
            psu13 = Psu(psu_name="Corsair Vengeance 650M", manufacturer="Corsair", wattage=650,
                        efficiency_rating="80+ Silver", modular="Semi", msrp=90, ReleaseDate=date(2019, 8, 1))
            psu14 = Psu(psu_name="Corsair Vengeance 750M", manufacturer="Corsair", wattage=750,
                        efficiency_rating="80+ Silver", modular="Semi", msrp=100, ReleaseDate=date(2019, 8, 1))
            psu15 = Psu(psu_name="Corsair TX750M", manufacturer="Corsair", wattage=750, efficiency_rating="80+ Gold",
                        modular="Semi", msrp=100, ReleaseDate=date(2019, 9, 1))

            # EVGA PSUs
            psu16 = Psu(psu_name="EVGA SuperNOVA 550 BP", manufacturer="EVGA", wattage=550,
                        efficiency_rating="80+ Bronze", modular="No", msrp=60, ReleaseDate=date(2020, 11, 18))
            psu17 = Psu(psu_name="EVGA SuperNOVA 650 BP", manufacturer="EVGA", wattage=650,
                        efficiency_rating="80+ Bronze", modular="No", msrp=75, ReleaseDate=date(2020, 11, 18))
            psu18 = Psu(psu_name="EVGA SuperNOVA 750 BP", manufacturer="EVGA", wattage=750,
                        efficiency_rating="80+ Bronze", modular="No", msrp=90, ReleaseDate=date(2020, 11, 18))
            psu19 = Psu(psu_name="EVGA SuperNOVA 650 G5", manufacturer="EVGA", wattage=650,
                        efficiency_rating="80+ Gold", modular="Fully", msrp=129, ReleaseDate=date(2019, 7, 9))
            psu20 = Psu(psu_name="EVGA SuperNOVA 750 G5", manufacturer="EVGA", wattage=750,
                        efficiency_rating="80+ Gold", modular="Fully", msrp=139, ReleaseDate=date(2019, 7, 9))
            psu21 = Psu(psu_name="EVGA SuperNOVA 850 G5", manufacturer="EVGA", wattage=850,
                        efficiency_rating="80+ Gold", modular="Fully", msrp=149, ReleaseDate=date(2019, 7, 9))
            psu22 = Psu(psu_name="EVGA SuperNOVA 1000 G5", manufacturer="EVGA", wattage=1000,
                        efficiency_rating="80+ Gold", modular="Fully", msrp=179, ReleaseDate=date(2019, 7, 9))
            psu23 = Psu(psu_name="EVGA SuperNOVA 750 G6", manufacturer="EVGA", wattage=750,
                        efficiency_rating="80+ Gold", modular="Fully", msrp=139, ReleaseDate=date(2021, 5, 5))
            psu24 = Psu(psu_name="EVGA SuperNOVA 850 G6", manufacturer="EVGA", wattage=850,
                        efficiency_rating="80+ Gold", modular="Fully", msrp=149, ReleaseDate=date(2021, 5, 5))
            psu25 = Psu(psu_name="EVGA SuperNOVA 1000 G6", manufacturer="EVGA", wattage=1000,
                        efficiency_rating="80+ Gold", modular="Fully", msrp=179, ReleaseDate=date(2021, 5, 5))
            psu26 = Psu(psu_name="EVGA SuperNOVA 750 GT", manufacturer="EVGA", wattage=750,
                        efficiency_rating="80+ Gold", modular="Fully", msrp=129, ReleaseDate=date(2021, 8, 17))
            psu27 = Psu(psu_name="EVGA SuperNOVA 850 GT", manufacturer="EVGA", wattage=850,
                        efficiency_rating="80+ Gold", modular="Fully", msrp=149, ReleaseDate=date(2021, 3, 18))
            psu28 = Psu(psu_name="EVGA SuperNOVA 1000 GT", manufacturer="EVGA", wattage=1000,
                        efficiency_rating="80+ Gold", modular="Fully", msrp=179, ReleaseDate=date(2021, 8, 17))
            psu29 = Psu(psu_name="EVGA SuperNOVA 850 P6", manufacturer="EVGA", wattage=850,
                        efficiency_rating="80+ Platinum", modular="Fully", msrp=179, ReleaseDate=date(2021, 7, 15))
            psu30 = Psu(psu_name="EVGA SuperNOVA 1000 P6", manufacturer="EVGA", wattage=1000,
                        efficiency_rating="80+ Platinum", modular="Fully", msrp=219, ReleaseDate=date(2021, 7, 15))

            # Seasonic PSUs
            psu31 = Psu(psu_name="Seasonic S12III 550", manufacturer="Seasonic", wattage=550,
                        efficiency_rating="80+ Bronze", modular="No", msrp=60, ReleaseDate=date(2019, 3, 15))
            psu32 = Psu(psu_name="Seasonic CORE GM 650", manufacturer="Seasonic", wattage=650,
                        efficiency_rating="80+ Gold", modular="Semi", msrp=75, ReleaseDate=date(2021, 1, 27))
            psu33 = Psu(psu_name="Seasonic CORE GX 550", manufacturer="Seasonic", wattage=550,
                        efficiency_rating="80+ Gold", modular="Fully", msrp=70, ReleaseDate=date(2021, 1, 27))
            psu34 = Psu(psu_name="Seasonic CORE GC 650", manufacturer="Seasonic", wattage=650,
                        efficiency_rating="80+ Gold", modular="No", msrp=65, ReleaseDate=date(2019, 7, 1))
            psu35 = Psu(psu_name="Seasonic FOCUS GX 750", manufacturer="Seasonic", wattage=750,
                        efficiency_rating="80+ Gold", modular="Fully", msrp=120, ReleaseDate=date(2019, 6, 1))
            psu36 = Psu(psu_name="Seasonic FOCUS GM 650", manufacturer="Seasonic", wattage=650,
                        efficiency_rating="80+ Gold", modular="Semi", msrp=100, ReleaseDate=date(2019, 6, 1))
            psu37 = Psu(psu_name="Seasonic FOCUS PX 850", manufacturer="Seasonic", wattage=850,
                        efficiency_rating="80+ Platinum", modular="Fully", msrp=150, ReleaseDate=date(2019, 6, 1))
            psu38 = Psu(psu_name="Seasonic FOCUS SGX 650", manufacturer="Seasonic", wattage=650,
                        efficiency_rating="80+ Gold", modular="Fully", msrp=130, ReleaseDate=date(2019, 6, 1))
            psu39 = Psu(psu_name="Seasonic PRIME GX 750", manufacturer="Seasonic", wattage=750,
                        efficiency_rating="80+ Gold", modular="Fully", msrp=160, ReleaseDate=date(2019, 8, 1))
            psu40 = Psu(psu_name="Seasonic PRIME PX 1000", manufacturer="Seasonic", wattage=1000,
                        efficiency_rating="80+ Platinum", modular="Fully", msrp=220, ReleaseDate=date(2019, 8, 1))
            psu41 = Psu(psu_name="Seasonic PRIME TX 850", manufacturer="Seasonic", wattage=850,
                        efficiency_rating="80+ Titanium", modular="Fully", msrp=230, ReleaseDate=date(2019, 8, 1))
            psu42 = Psu(psu_name="Seasonic PRIME TX 1000", manufacturer="Seasonic", wattage=1000,
                        efficiency_rating="80+ Titanium", modular="Fully", msrp=280, ReleaseDate=date(2020, 5, 1))

            # Cooler Master PSUs
            psu43 = Psu(psu_name="Cooler Master MWE Bronze 550 V2", manufacturer="Cooler Master", wattage=550,
                        efficiency_rating="80+ Bronze", modular="No", msrp=60, ReleaseDate=date(2020, 6, 1))
            psu44 = Psu(psu_name="Cooler Master MWE Bronze 650 V2", manufacturer="Cooler Master", wattage=650,
                        efficiency_rating="80+ Bronze", modular="No", msrp=70, ReleaseDate=date(2020, 6, 1))
            psu45 = Psu(psu_name="Cooler Master MWE Bronze 750 V2", manufacturer="Cooler Master", wattage=750,
                        efficiency_rating="80+ Bronze", modular="No", msrp=80, ReleaseDate=date(2020, 6, 1))
            psu46 = Psu(psu_name="Cooler Master MWE Gold 650 V2", manufacturer="Cooler Master", wattage=650,
                        efficiency_rating="80+ Gold", modular="Fully", msrp=90, ReleaseDate=date(2020, 7, 1))
            psu47 = Psu(psu_name="Cooler Master MWE Gold 750 V2", manufacturer="Cooler Master", wattage=750,
                        efficiency_rating="80+ Gold", modular="Fully", msrp=110, ReleaseDate=date(2020, 7, 1))
            psu48 = Psu(psu_name="Cooler Master MWE Gold 850 V2", manufacturer="Cooler Master", wattage=850,
                        efficiency_rating="80+ Gold", modular="Fully", msrp=130, ReleaseDate=date(2020, 7, 1))
            psu49 = Psu(psu_name="Cooler Master V650 SFX Gold", manufacturer="Cooler Master", wattage=650,
                        efficiency_rating="80+ Gold", modular="Fully", msrp=129, ReleaseDate=date(2021, 1, 1))
            psu50 = Psu(psu_name="Cooler Master V750 Gold V2", manufacturer="Cooler Master", wattage=750,
                        efficiency_rating="80+ Gold", modular="Fully", msrp=139, ReleaseDate=date(2020, 9, 1))
            psu51 = Psu(psu_name="Cooler Master V850 Gold V2", manufacturer="Cooler Master", wattage=850,
                        efficiency_rating="80+ Gold", modular="Fully", msrp=159, ReleaseDate=date(2020, 9, 1))
            psu52 = Psu(psu_name="Cooler Master V850 Platinum", manufacturer="Cooler Master", wattage=850,
                        efficiency_rating="80+ Platinum", modular="Fully", msrp=199, ReleaseDate=date(2019, 11, 1))
            psu53 = Psu(psu_name="Cooler Master V1000 Platinum", manufacturer="Cooler Master", wattage=1000,
                        efficiency_rating="80+ Platinum", modular="Fully", msrp=239, ReleaseDate=date(2020, 1, 15))
            psu54 = Psu(psu_name="Cooler Master MasterWatt 750", manufacturer="Cooler Master", wattage=750,
                        efficiency_rating="80+ Bronze", modular="Semi", msrp=85, ReleaseDate=date(2019, 9, 1))

            # Be Quiet! PSUs
            psu55 = Psu(psu_name="Be Quiet! Pure Power 11 500W", manufacturer="Be Quiet!", wattage=500,
                        efficiency_rating="80+ Gold", modular="No", msrp=80, ReleaseDate=date(2019, 1, 10))
            psu56 = Psu(psu_name="Be Quiet! Pure Power 11 CM 700W", manufacturer="Be Quiet!", wattage=700,
                        efficiency_rating="80+ Gold", modular="Semi", msrp=120, ReleaseDate=date(2019, 1, 10))
            psu57 = Psu(psu_name="Be Quiet! Pure Power 11 FM 750W", manufacturer="Be Quiet!", wattage=750,
                        efficiency_rating="80+ Gold", modular="Fully", msrp=130, ReleaseDate=date(2021, 8, 1))
            psu58 = Psu(psu_name="Be Quiet! Straight Power 11 650W", manufacturer="Be Quiet!", wattage=650,
                        efficiency_rating="80+ Gold", modular="Fully", msrp=130, ReleaseDate=date(2019, 7, 1))
            psu59 = Psu(psu_name="Be Quiet! Straight Power 11 Platinum 1200W", manufacturer="Be Quiet!", wattage=1200,
                        efficiency_rating="80+ Platinum", modular="Fully", msrp=250, ReleaseDate=date(2020, 3, 1))
            psu60 = Psu(psu_name="Be Quiet! Dark Power 12 850W", manufacturer="Be Quiet!", wattage=850,
                        efficiency_rating="80+ Titanium", modular="Fully", msrp=239, ReleaseDate=date(2021, 3, 9))
            psu61 = Psu(psu_name="Be Quiet! Dark Power 12 1000W", manufacturer="Be Quiet!", wattage=1000,
                        efficiency_rating="80+ Titanium", modular="Fully", msrp=279, ReleaseDate=date(2021, 3, 9))
            psu62 = Psu(psu_name="Be Quiet! Dark Power Pro 12 1200W", manufacturer="Be Quiet!", wattage=1200,
                        efficiency_rating="80+ Titanium", modular="Fully", msrp=399, ReleaseDate=date(2020, 9, 8))
            psu63 = Psu(psu_name="Be Quiet! System Power 9 600W", manufacturer="Be Quiet!", wattage=600,
                        efficiency_rating="80+ Bronze", modular="No", msrp=70, ReleaseDate=date(2019, 2, 1))

            # ASUS PSUs
            psu64 = Psu(psu_name="ASUS ROG Strix 650W Gold", manufacturer="ASUS", wattage=650,
                        efficiency_rating="80+ Gold", modular="Fully", msrp=120, ReleaseDate=date(2020, 8, 1))
            psu65 = Psu(psu_name="ASUS ROG Strix 750W Gold", manufacturer="ASUS", wattage=750,
                        efficiency_rating="80+ Gold", modular="Fully", msrp=130, ReleaseDate=date(2019, 10, 1))
            psu66 = Psu(psu_name="ASUS ROG Thor 850W Platinum", manufacturer="ASUS", wattage=850,
                        efficiency_rating="80+ Platinum", modular="Fully", msrp=200, ReleaseDate=date(2019, 1, 10))
            psu67 = Psu(psu_name="ASUS ROG Thor 1200W Platinum", manufacturer="ASUS", wattage=1200,
                        efficiency_rating="80+ Platinum", modular="Fully", msrp=250, ReleaseDate=date(2019, 1, 10))
            psu68 = Psu(psu_name="ASUS TUF Gaming 650B", manufacturer="ASUS", wattage=650,
                        efficiency_rating="80+ Bronze", modular="No", msrp=80, ReleaseDate=date(2020, 7, 1))
            psu69 = Psu(psu_name="ASUS TUF Gaming 750B", manufacturer="ASUS", wattage=750,
                        efficiency_rating="80+ Bronze", modular="No", msrp=90, ReleaseDate=date(2020, 7, 1))

            # Gigabyte PSUs
            psu70 = Psu(psu_name="Gigabyte GP-P550B", manufacturer="Gigabyte", wattage=550,
                        efficiency_rating="80+ Bronze", modular="No", msrp=50, ReleaseDate=date(2019, 6, 1))
            psu71 = Psu(psu_name="Gigabyte GP-P650B", manufacturer="Gigabyte", wattage=650,
                        efficiency_rating="80+ Bronze", modular="No", msrp=60, ReleaseDate=date(2019, 6, 1))
            psu72 = Psu(psu_name="Gigabyte GP-P750B", manufacturer="Gigabyte", wattage=750,
                        efficiency_rating="80+ Bronze", modular="No", msrp=80, ReleaseDate=date(2019, 6, 1))
            psu73 = Psu(psu_name="Gigabyte GP-P750GM", manufacturer="Gigabyte", wattage=750,
                        efficiency_rating="80+ Gold", modular="Fully", msrp=99, ReleaseDate=date(2020, 7, 1))
            psu74 = Psu(psu_name="Gigabyte GP-P850GM", manufacturer="Gigabyte", wattage=850,
                        efficiency_rating="80+ Gold", modular="Fully", msrp=119, ReleaseDate=date(2020, 7, 1))

            # NZXT PSUs
            psu75 = Psu(psu_name="NZXT C650 Gold", manufacturer="NZXT", wattage=650, efficiency_rating="80+ Gold",
                        modular="Fully", msrp=110, ReleaseDate=date(2020, 2, 1))
            psu76 = Psu(psu_name="NZXT C750 Gold", manufacturer="NZXT", wattage=750, efficiency_rating="80+ Gold",
                        modular="Fully", msrp=130, ReleaseDate=date(2020, 2, 1))
            psu77 = Psu(psu_name="NZXT C850 Gold", manufacturer="NZXT", wattage=850, efficiency_rating="80+ Gold",
                        modular="Fully", msrp=150, ReleaseDate=date(2020, 2, 1))
            psu78 = Psu(psu_name="NZXT C550 Bronze", manufacturer="NZXT", wattage=550, efficiency_rating="80+ Bronze",
                        modular="Semi", msrp=80, ReleaseDate=date(2021, 8, 1))
            psu79 = Psu(psu_name="NZXT C650 Bronze", manufacturer="NZXT", wattage=650, efficiency_rating="80+ Bronze",
                        modular="Semi", msrp=90, ReleaseDate=date(2021, 8, 1))
            psu80 = Psu(psu_name="NZXT C750 Bronze", manufacturer="NZXT", wattage=750, efficiency_rating="80+ Bronze",
                        modular="Semi", msrp=100, ReleaseDate=date(2021, 8, 1))

            # MSI PSUs
            psu81 = Psu(psu_name="MSI MAG A550BN", manufacturer="MSI", wattage=550, efficiency_rating="80+ Bronze",
                        modular="No", msrp=60, ReleaseDate=date(2020, 7, 1))
            psu82 = Psu(psu_name="MSI MAG A650BN", manufacturer="MSI", wattage=650, efficiency_rating="80+ Bronze",
                        modular="No", msrp=70, ReleaseDate=date(2020, 7, 1))
            psu83 = Psu(psu_name="MSI MPG A650GF", manufacturer="MSI", wattage=650, efficiency_rating="80+ Gold",
                        modular="Fully", msrp=100, ReleaseDate=date(2020, 9, 1))
            psu84 = Psu(psu_name="MSI MPG A750GF", manufacturer="MSI", wattage=750, efficiency_rating="80+ Gold",
                        modular="Fully", msrp=120, ReleaseDate=date(2020, 9, 1))
            psu85 = Psu(psu_name="MSI MPG A850GF", manufacturer="MSI", wattage=850, efficiency_rating="80+ Gold",
                        modular="Fully", msrp=140, ReleaseDate=date(2020, 9, 1))

            # Thermaltake PSUs
            psu86 = Psu(psu_name="Thermaltake Smart BX1 650W", manufacturer="Thermaltake", wattage=650,
                        efficiency_rating="80+ Bronze", modular="No", msrp=70, ReleaseDate=date(2019, 3, 1))
            psu87 = Psu(psu_name="Thermaltake Smart BX1 750W", manufacturer="Thermaltake", wattage=750,
                        efficiency_rating="80+ Bronze", modular="No", msrp=80, ReleaseDate=date(2019, 3, 1))
            psu88 = Psu(psu_name="Thermaltake Smart BM2 750W", manufacturer="Thermaltake", wattage=750,
                        efficiency_rating="80+ Bronze", modular="Semi", msrp=85, ReleaseDate=date(2020, 5, 1))
            psu89 = Psu(psu_name="Thermaltake Toughpower GF1 650W", manufacturer="Thermaltake", wattage=650,
                        efficiency_rating="80+ Gold", modular="Fully", msrp=120, ReleaseDate=date(2019, 7, 1))
            psu90 = Psu(psu_name="Thermaltake Toughpower GF1 750W", manufacturer="Thermaltake", wattage=750,
                        efficiency_rating="80+ Gold", modular="Fully", msrp=130, ReleaseDate=date(2019, 7, 1))
            psu91 = Psu(psu_name="Thermaltake Toughpower GF1 850W", manufacturer="Thermaltake", wattage=850,
                        efficiency_rating="80+ Gold", modular="Fully", msrp=150, ReleaseDate=date(2019, 7, 1))
            psu92 = Psu(psu_name="Thermaltake Toughpower Grand RGB 1200W Platinum", manufacturer="Thermaltake",
                        wattage=1200, efficiency_rating="80+ Platinum", modular="Fully", msrp=250,
                        ReleaseDate=date(2019, 10, 1))
            psu93 = Psu(psu_name="Thermaltake Toughpower PF1 ARGB 850W Platinum", manufacturer="Thermaltake",
                        wattage=850, efficiency_rating="80+ Platinum", modular="Fully", msrp=180,
                        ReleaseDate=date(2020, 6, 1))

            # SilverStone PSUs
            psu94 = Psu(psu_name="SilverStone ET550-B", manufacturer="SilverStone", wattage=550,
                        efficiency_rating="80+ Bronze", modular="No", msrp=50, ReleaseDate=date(2019, 4, 1))
            psu95 = Psu(psu_name="SilverStone Strider Gold S 750W", manufacturer="SilverStone", wattage=750,
                        efficiency_rating="80+ Gold", modular="Fully", msrp=130, ReleaseDate=date(2019, 9, 1))
            psu96 = Psu(psu_name="SilverStone Strider Platinum 850W", manufacturer="SilverStone", wattage=850,
                        efficiency_rating="80+ Platinum", modular="Fully", msrp=160, ReleaseDate=date(2020, 6, 1))
            psu97 = Psu(psu_name="SilverStone Strider Titanium 1100W", manufacturer="SilverStone", wattage=1100,
                        efficiency_rating="80+ Titanium", modular="Fully", msrp=250, ReleaseDate=date(2019, 6, 1))
            psu98 = Psu(psu_name="SilverStone Strider Platinum 1200W", manufacturer="SilverStone", wattage=1200,
                        efficiency_rating="80+ Platinum", modular="Fully", msrp=250, ReleaseDate=date(2019, 11, 1))

            # Antec PSUs
            psu99 = Psu(psu_name="Antec EarthWatts Gold Pro 650W", manufacturer="Antec", wattage=650,
                        efficiency_rating="80+ Gold", modular="Semi", msrp=80, ReleaseDate=date(2019, 4, 1))
            psu100 = Psu(psu_name="Antec EarthWatts Gold Pro 750W", manufacturer="Antec", wattage=750,
                         efficiency_rating="80+ Gold", modular="Semi", msrp=100, ReleaseDate=date(2019, 4, 1))
            psu101 = Psu(psu_name="Antec NeoECO Gold ZEN 700W", manufacturer="Antec", wattage=700,
                         efficiency_rating="80+ Gold", modular="No", msrp=90, ReleaseDate=date(2020, 6, 1))
            psu102 = Psu(psu_name="Antec High Current Gamer 850W Gold", manufacturer="Antec", wattage=850,
                         efficiency_rating="80+ Gold", modular="Fully", msrp=150, ReleaseDate=date(2019, 3, 1))
            psu103 = Psu(psu_name="Antec Signature Platinum 1000W", manufacturer="Antec", wattage=1000,
                         efficiency_rating="80+ Platinum", modular="Fully", msrp=230, ReleaseDate=date(2019, 5, 1))

            # FSP PSUs
            psu104 = Psu(psu_name="FSP Hydro G 750W", manufacturer="FSP", wattage=750, efficiency_rating="80+ Gold",
                         modular="Fully", msrp=130, ReleaseDate=date(2019, 4, 1))
            psu105 = Psu(psu_name="FSP Hydro PTM 850W", manufacturer="FSP", wattage=850,
                         efficiency_rating="80+ Platinum", modular="Fully", msrp=180, ReleaseDate=date(2019, 4, 1))
            psu106 = Psu(psu_name="FSP Hydro PTM 1200W", manufacturer="FSP", wattage=1200,
                         efficiency_rating="80+ Platinum", modular="Fully", msrp=250, ReleaseDate=date(2020, 7, 1))
            psu107 = Psu(psu_name="FSP Dagger 600W", manufacturer="FSP", wattage=600, efficiency_rating="80+ Gold",
                         modular="Fully", msrp=140, ReleaseDate=date(2019, 2, 1))

            # XPG PSUs
            psu108 = Psu(psu_name="XPG Pylon 550W", manufacturer="XPG", wattage=550, efficiency_rating="80+ Bronze",
                         modular="No", msrp=60, ReleaseDate=date(2020, 7, 1))
            psu109 = Psu(psu_name="XPG Core Reactor 750W", manufacturer="XPG", wattage=750,
                         efficiency_rating="80+ Gold", modular="Fully", msrp=120, ReleaseDate=date(2020, 3, 1))
            psu110 = Psu(psu_name="XPG Core Reactor 850W", manufacturer="XPG", wattage=850,
                         efficiency_rating="80+ Gold", modular="Fully", msrp=140, ReleaseDate=date(2020, 3, 1))

            # Super Flower PSUs
            psu111 = Psu(psu_name="Super Flower Leadex III 750W", manufacturer="Super Flower", wattage=750,
                         efficiency_rating="80+ Gold", modular="Fully", msrp=130, ReleaseDate=date(2019, 5, 1))
            psu112 = Psu(psu_name="Super Flower Leadex Platinum 1000W", manufacturer="Super Flower", wattage=1000,
                         efficiency_rating="80+ Platinum", modular="Fully", msrp=220, ReleaseDate=date(2019, 5, 1))

            # Fractal Design PSUs
            psu113 = Psu(psu_name="Fractal Design Ion+ 760W Platinum", manufacturer="Fractal Design", wattage=760,
                         efficiency_rating="80+ Platinum", modular="Fully", msrp=160, ReleaseDate=date(2019, 7, 1))
            psu114 = Psu(psu_name="Fractal Design Ion+ 860W Platinum", manufacturer="Fractal Design", wattage=860,
                         efficiency_rating="80+ Platinum", modular="Fully", msrp=180, ReleaseDate=date(2019, 7, 1))

            # Enermax PSUs
            psu115 = Psu(psu_name="Enermax Revolution DF 750W", manufacturer="Enermax", wattage=750,
                         efficiency_rating="80+ Gold", modular="Fully", msrp=130, ReleaseDate=date(2019, 8, 1))
            psu116 = Psu(psu_name="Enermax MaxTytan 800W", manufacturer="Enermax", wattage=800,
                         efficiency_rating="80+ Titanium", modular="Fully", msrp=230, ReleaseDate=date(2019, 8, 1))

            # DeepCool PSUs
            psu117 = Psu(psu_name="DeepCool DQ650-M", manufacturer="DeepCool", wattage=650,
                         efficiency_rating="80+ Gold", modular="Fully", msrp=90, ReleaseDate=date(2019, 4, 1))
            psu118 = Psu(psu_name="DeepCool DQ750-M", manufacturer="DeepCool", wattage=750,
                         efficiency_rating="80+ Gold", modular="Fully", msrp=110, ReleaseDate=date(2019, 4, 1))

            # Cougar PSUs
            psu119 = Psu(psu_name="Cougar GX-F 650W", manufacturer="Cougar", wattage=650, efficiency_rating="80+ Gold",
                         modular="Fully", msrp=100, ReleaseDate=date(2019, 3, 1))
            psu120 = Psu(psu_name="Cougar VTE600", manufacturer="Cougar", wattage=600, efficiency_rating="80+ Bronze",
                         modular="No", msrp=60, ReleaseDate=date(2019, 3, 1))

            # Add all PSU entries to the session
            db.session.add_all(
                [psu1, psu2, psu3, psu4, psu5, psu6, psu7, psu8, psu9, psu10, psu11, psu12, psu13, psu14, psu15, psu16,
                 psu17, psu18, psu19, psu20, psu21, psu22, psu23, psu24, psu25, psu26, psu27, psu28, psu29, psu30,
                 psu31, psu32, psu33, psu34, psu35, psu36, psu37, psu38, psu39, psu40, psu41, psu42, psu43, psu44,
                 psu45, psu46, psu47, psu48, psu49, psu50, psu51, psu52, psu53, psu54, psu55, psu56, psu57, psu58,
                 psu59, psu60, psu61, psu62, psu63, psu64, psu65, psu66, psu67, psu68, psu69, psu70, psu71, psu72,
                 psu73, psu74, psu75, psu76, psu77, psu78, psu79, psu80, psu81, psu82, psu83, psu84, psu85, psu86,
                 psu87, psu88, psu89, psu90, psu91, psu92, psu93, psu94, psu95, psu96, psu97, psu98, psu99, psu100,
                 psu101, psu102, psu103, psu104, psu105, psu106, psu107, psu108, psu109, psu110, psu111, psu112, psu113,
                 psu114, psu115, psu116, psu117, psu118, psu119, psu120])

        if not Case.query.first():  # Check if the Case table is empty
            case1 = Case(case_name="NZXT H510", manufacturer="NZXT", form_factor="Mid Tower", color="Black", msrp=70,
                         ReleaseDate=date(2019, 7, 1))
            case2 = Case(case_name="Corsair 4000D Airflow", manufacturer="Corsair", form_factor="Mid Tower",
                         color="White", msrp=95, ReleaseDate=date(2020, 9, 15))
            case3 = Case(case_name="Fractal Design Meshify C", manufacturer="Fractal Design", form_factor="Mid Tower",
                         color="Black", msrp=90, ReleaseDate=date(2019, 3, 12))
            case4 = Case(case_name="Lian Li PC-O11 Dynamic", manufacturer="Lian Li", form_factor="Mid Tower",
                         color="Black", msrp=140, ReleaseDate=date(2019, 5, 18))
            case5 = Case(case_name="Phanteks Eclipse P400A", manufacturer="Phanteks", form_factor="Mid Tower",
                         color="Black", msrp=70, ReleaseDate=date(2019, 8, 22))
            case6 = Case(case_name="Cooler Master MasterBox Q300L", manufacturer="Cooler Master",
                         form_factor="Micro-ATX", color="Black", msrp=50, ReleaseDate=date(2019, 2, 14))
            case7 = Case(case_name="Thermaltake Core V1", manufacturer="Thermaltake", form_factor="Mini-ITX",
                         color="Black", msrp=50, ReleaseDate=date(2019, 4, 5))
            case8 = Case(case_name="be quiet! Pure Base 500", manufacturer="be quiet!", form_factor="Mid Tower",
                         color="Black", msrp=80, ReleaseDate=date(2019, 9, 3))
            case9 = Case(case_name="Corsair Crystal 570X RGB", manufacturer="Corsair", form_factor="Mid Tower",
                         color="Black", msrp=180, ReleaseDate=date(2019, 1, 15))
            case10 = Case(case_name="NZXT H210", manufacturer="NZXT", form_factor="Mini-ITX", color="White", msrp=80,
                          ReleaseDate=date(2019, 7, 15))

            case11 = Case(case_name="Fractal Design Define 7", manufacturer="Fractal Design", form_factor="Mid Tower",
                          color="Black", msrp=170, ReleaseDate=date(2020, 2, 11))
            case12 = Case(case_name="Cooler Master NR200", manufacturer="Cooler Master", form_factor="Mini-ITX",
                          color="Black", msrp=80, ReleaseDate=date(2020, 7, 14))
            case13 = Case(case_name="Lian Li Lancool II Mesh", manufacturer="Lian Li", form_factor="Mid Tower",
                          color="Black", msrp=90, ReleaseDate=date(2020, 6, 20))
            case14 = Case(case_name="Phanteks P500A", manufacturer="Phanteks", form_factor="Full Tower", color="White",
                          msrp=100, ReleaseDate=date(2020, 7, 7))
            case15 = Case(case_name="NZXT H710i", manufacturer="NZXT", form_factor="Mid Tower", color="Black/Red",
                          msrp=170, ReleaseDate=date(2019, 10, 22))
            case16 = Case(case_name="Corsair iCUE 465X RGB", manufacturer="Corsair", form_factor="Mid Tower",
                          color="White", msrp=120, ReleaseDate=date(2019, 10, 10))
            case17 = Case(case_name="Fractal Design Meshify S2", manufacturer="Fractal Design", form_factor="Mid Tower",
                          color="Black", msrp=150, ReleaseDate=date(2019, 1, 22))
            case18 = Case(case_name="be quiet! Dark Base 700", manufacturer="be quiet!", form_factor="Mid Tower",
                          color="Black", msrp=180, ReleaseDate=date(2019, 3, 5))
            case19 = Case(case_name="Thermaltake View 71 TG", manufacturer="Thermaltake", form_factor="Full Tower",
                          color="Black", msrp=170, ReleaseDate=date(2019, 4, 23))
            case20 = Case(case_name="Cooler Master H500", manufacturer="Cooler Master", form_factor="Mid Tower",
                          color="Gray", msrp=100, ReleaseDate=date(2019, 2, 28))

            case21 = Case(case_name="NZXT H1", manufacturer="NZXT", form_factor="Mini-ITX", color="Black", msrp=350,
                          ReleaseDate=date(2020, 2, 26))
            case22 = Case(case_name="Corsair 220T RGB", manufacturer="Corsair", form_factor="Mid Tower", color="Black",
                          msrp=110, ReleaseDate=date(2019, 11, 14))
            case23 = Case(case_name="Phanteks Evolv Shift", manufacturer="Phanteks", form_factor="Mini-ITX",
                          color="Silver", msrp=110, ReleaseDate=date(2019, 5, 17))
            case24 = Case(case_name="Lian Li O11 Dynamic Mini", manufacturer="Lian Li", form_factor="Micro-ATX",
                          color="Black", msrp=100, ReleaseDate=date(2020, 11, 11))
            case25 = Case(case_name="Fractal Design Era ITX", manufacturer="Fractal Design", form_factor="Mini-ITX",
                          color="Gold", msrp=160, ReleaseDate=date(2020, 3, 31))
            case26 = Case(case_name="be quiet! Silent Base 802", manufacturer="be quiet!", form_factor="Mid Tower",
                          color="Black", msrp=160, ReleaseDate=date(2020, 10, 20))
            case27 = Case(case_name="Cooler Master TD500 Mesh", manufacturer="Cooler Master", form_factor="Mid Tower",
                          color="Black", msrp=100, ReleaseDate=date(2020, 4, 7))
            case28 = Case(case_name="Thermaltake Level 20 MT", manufacturer="Thermaltake", form_factor="Mid Tower",
                          color="Black", msrp=90, ReleaseDate=date(2019, 8, 9))
            case29 = Case(case_name="NZXT H510 Elite", manufacturer="NZXT", form_factor="Mid Tower", color="White",
                          msrp=150, ReleaseDate=date(2019, 7, 22))
            case30 = Case(case_name="Corsair 275R Airflow", manufacturer="Corsair", form_factor="Mid Tower",
                          color="Black", msrp=80, ReleaseDate=date(2019, 12, 5))

            case31 = Case(case_name="Phanteks Enthoo Pro 2", manufacturer="Phanteks", form_factor="Full Tower",
                          color="Black", msrp=140, ReleaseDate=date(2020, 8, 14))
            case32 = Case(case_name="Lian Li PC-011 Dynamic XL", manufacturer="Lian Li", form_factor="Full Tower",
                          color="White", msrp=200, ReleaseDate=date(2019, 9, 17))
            case33 = Case(case_name="Fractal Design Define 7 Compact", manufacturer="Fractal Design",
                          form_factor="Mid Tower", color="Black", msrp=110, ReleaseDate=date(2020, 5, 28))
            case34 = Case(case_name="be quiet! Pure Base 500DX", manufacturer="be quiet!", form_factor="Mid Tower",
                          color="White", msrp=100, ReleaseDate=date(2020, 4, 28))
            case35 = Case(case_name="Cooler Master MasterCase H500M", manufacturer="Cooler Master",
                          form_factor="Mid Tower", color="Black", msrp=200, ReleaseDate=date(2019, 6, 11))
            case36 = Case(case_name="Thermaltake Tower 900", manufacturer="Thermaltake", form_factor="Super Tower",
                          color="Black", msrp=280, ReleaseDate=date(2019, 5, 5))
            case37 = Case(case_name="NZXT H710", manufacturer="NZXT", form_factor="Mid Tower", color="Black", msrp=140,
                          ReleaseDate=date(2019, 10, 15))
            case38 = Case(case_name="Corsair 680X RGB", manufacturer="Corsair", form_factor="Mid Tower", color="Black",
                          msrp=250, ReleaseDate=date(2019, 3, 19))
            case39 = Case(case_name="Phanteks Enthoo Evolv X", manufacturer="Phanteks", form_factor="Mid Tower",
                          color="Gray", msrp=200, ReleaseDate=date(2019, 2, 7))
            case40 = Case(case_name="Fractal Design Node 202", manufacturer="Fractal Design", form_factor="Mini-ITX",
                          color="Black", msrp=80, ReleaseDate=date(2019, 3, 28))

            case41 = Case(case_name="Cooler Master SL600M", manufacturer="Cooler Master", form_factor="Mid Tower",
                          color="Black", msrp=200, ReleaseDate=date(2019, 4, 16))
            case42 = Case(case_name="be quiet! Shadow Base 601", manufacturer="be quiet!", form_factor="Mid Tower",
                          color="Silver", msrp=150, ReleaseDate=date(2019, 11, 26))
            case43 = Case(case_name="Lian Li TU150", manufacturer="Lian Li", form_factor="Mini-ITX", color="Black",
                          msrp=110, ReleaseDate=date(2019, 8, 27))
            case44 = Case(case_name="NZXT H210i", manufacturer="NZXT", form_factor="Mini-ITX", color="Black/Red",
                          msrp=110, ReleaseDate=date(2019, 7, 18))
            case45 = Case(case_name="Thermaltake Core P3", manufacturer="Thermaltake", form_factor="Mid Tower",
                          color="Black", msrp=130, ReleaseDate=date(2019, 9, 24))
            case46 = Case(case_name="Corsair 465X RGB", manufacturer="Corsair", form_factor="Mid Tower", color="Black",
                          msrp=150, ReleaseDate=date(2019, 10, 24))
            case47 = Case(case_name="Phanteks Eclipse P300A", manufacturer="Phanteks", form_factor="Mid Tower",
                          color="Black", msrp=60, ReleaseDate=date(2020, 1, 23))
            case48 = Case(case_name="Fractal Design Meshify 2", manufacturer="Fractal Design", form_factor="Mid Tower",
                          color="Black", msrp=140, ReleaseDate=date(2020, 11, 17))
            case49 = Case(case_name="Cooler Master MasterBox TD500", manufacturer="Cooler Master",
                          form_factor="Mid Tower", color="White", msrp=100, ReleaseDate=date(2020, 3, 17))
            case50 = Case(case_name="be quiet! Pure Base 600", manufacturer="be quiet!", form_factor="Mid Tower",
                          color="Black", msrp=90, ReleaseDate=date(2019, 4, 9))

            case51 = Case(case_name="NZXT H200", manufacturer="NZXT", form_factor="Mini-ITX", color="Black/Blue",
                          msrp=90, ReleaseDate=date(2019, 1, 8))
            case52 = Case(case_name="Corsair 175R RGB", manufacturer="Corsair", form_factor="Mid Tower", color="Black",
                          msrp=70, ReleaseDate=date(2019, 11, 5))
            case53 = Case(case_name="Lian Li PC-Q58", manufacturer="Lian Li", form_factor="Mini-ITX", color="Black",
                          msrp=130, ReleaseDate=date(2021, 8, 4))
            case54 = Case(case_name="Phanteks Evolv Shift 2", manufacturer="Phanteks", form_factor="Mini-ITX",
                          color="Black", msrp=120, ReleaseDate=date(2020, 12, 15))
            case55 = Case(case_name="Fractal Design Focus G", manufacturer="Fractal Design", form_factor="Mid Tower",
                          color="Blue", msrp=60, ReleaseDate=date(2019, 1, 30))
            case56 = Case(case_name="Cooler Master MasterBox MB311L", manufacturer="Cooler Master",
                          form_factor="Micro-ATX", color="Black", msrp=60, ReleaseDate=date(2020, 6, 2))
            case57 = Case(case_name="Thermaltake S100", manufacturer="Thermaltake", form_factor="Micro-ATX",
                          color="White", msrp=70, ReleaseDate=date(2020, 2, 18))
            case58 = Case(case_name="be quiet! Pure Base 500 Window", manufacturer="be quiet!", form_factor="Mid Tower",
                          color="Black", msrp=90, ReleaseDate=date(2019, 9, 10))
            case59 = Case(case_name="NZXT H400i", manufacturer="NZXT", form_factor="Micro-ATX", color="Black/Purple",
                          msrp=120, ReleaseDate=date(2019, 2, 12))
            case60 = Case(case_name="Corsair 110R", manufacturer="Corsair", form_factor="Mid Tower", color="Black",
                          msrp=65, ReleaseDate=date(2020, 1, 14))

            case61 = Case(case_name="Phanteks P300", manufacturer="Phanteks", form_factor="Mid Tower", color="Black",
                          msrp=60, ReleaseDate=date(2019, 1, 17))
            case62 = Case(case_name="Lian Li LANCOOL 215", manufacturer="Lian Li", form_factor="Mid Tower",
                          color="Black", msrp=90, ReleaseDate=date(2020, 9, 22))
            case63 = Case(case_name="Fractal Design North", manufacturer="Fractal Design", form_factor="Mid Tower",
                          color="Charcoal", msrp=130, ReleaseDate=date(2022, 6, 16))
            case64 = Case(case_name="be quiet! Dark Base Pro 901", manufacturer="be quiet!", form_factor="Full Tower",
                          color="Black", msrp=260, ReleaseDate=date(2023, 5, 23))
            case65 = Case(case_name="Cooler Master HAF 700", manufacturer="Cooler Master", form_factor="Full Tower",
                          color="Black", msrp=300, ReleaseDate=date(2022, 2, 15))
            case66 = Case(case_name="Thermaltake Divider 300 TG", manufacturer="Thermaltake", form_factor="Mid Tower",
                          color="White", msrp=120, ReleaseDate=date(2021, 3, 23))
            case67 = Case(case_name="NZXT H7 Flow", manufacturer="NZXT", form_factor="Mid Tower", color="Black",
                          msrp=130, ReleaseDate=date(2022, 5, 10))
            case68 = Case(case_name="Corsair 5000D Airflow", manufacturer="Corsair", form_factor="Mid Tower",
                          color="White", msrp=165, ReleaseDate=date(2021, 1, 28))
            case69 = Case(case_name="Phanteks Evolv X", manufacturer="Phanteks", form_factor="Mid Tower",
                          color="Silver", msrp=200, ReleaseDate=date(2019, 10, 15))
            case70 = Case(case_name="Lian Li A4-H20", manufacturer="Lian Li", form_factor="Mini-ITX", color="Black",
                          msrp=120, ReleaseDate=date(2022, 1, 18))

            case71 = Case(case_name="Fractal Design Pop XL Air", manufacturer="Fractal Design", form_factor="Mid Tower",
                          color="White", msrp=105, ReleaseDate=date(2022, 7, 19))
            case72 = Case(case_name="be quiet! Silent Base 601", manufacturer="be quiet!", form_factor="Mid Tower",
                          color="Orange", msrp=130, ReleaseDate=date(2019, 6, 4))
            case73 = Case(case_name="Cooler Master HAF 500", manufacturer="Cooler Master", form_factor="Mid Tower",
                          color="Black", msrp=150, ReleaseDate=date(2022, 2, 1))
            case74 = Case(case_name="Thermaltake View 51", manufacturer="Thermaltake", form_factor="Full Tower",
                          color="Snow", msrp=190, ReleaseDate=date(2020, 1, 7))
            case75 = Case(case_name="NZXT H9 Flow", manufacturer="NZXT", form_factor="Mid Tower", color="White",
                          msrp=160, ReleaseDate=date(2023, 1, 17))
            case76 = Case(case_name="Corsair 7000D Airflow", manufacturer="Corsair", form_factor="Full Tower",
                          color="Black", msrp=270, ReleaseDate=date(2021, 5, 13))
            case77 = Case(case_name="Phanteks Enthoo Pro II", manufacturer="Phanteks", form_factor="Full Tower",
                          color="Gray", msrp=150, ReleaseDate=date(2020, 8, 5))
            case78 = Case(case_name="Lian Li O11 Dynamic EVO", manufacturer="Lian Li", form_factor="Mid Tower",
                          color="Black", msrp=170, ReleaseDate=date(2022, 1, 12))
            case79 = Case(case_name="Fractal Design Torrent", manufacturer="Fractal Design", form_factor="Mid Tower",
                          color="Black", msrp=190, ReleaseDate=date(2021, 8, 18))
            case80 = Case(case_name="be quiet! Pure Base 600S", manufacturer="be quiet!", form_factor="Mid Tower",
                          color="Silver", msrp=120, ReleaseDate=date(2019, 7, 9))

            case81 = Case(case_name="Cooler Master CMP 510", manufacturer="Cooler Master", form_factor="Mid Tower",
                          color="Black", msrp=70, ReleaseDate=date(2020, 11, 10))
            case82 = Case(case_name="Thermaltake AH T600", manufacturer="Thermaltake", form_factor="Full Tower",
                          color="Black", msrp=250, ReleaseDate=date(2020, 3, 24))
            case83 = Case(case_name="NZXT H5 Flow", manufacturer="NZXT", form_factor="Mid Tower", color="Black",
                          msrp=95, ReleaseDate=date(2023, 4, 4))
            case84 = Case(case_name="Corsair iCUE 5000X", manufacturer="Corsair", form_factor="Mid Tower",
                          color="White", msrp=205, ReleaseDate=date(2021, 1, 19))
            case85 = Case(case_name="Phanteks Eclipse G360A", manufacturer="Phanteks", form_factor="Mid Tower",
                          color="Black", msrp=100, ReleaseDate=date(2022, 5, 17))
            case86 = Case(case_name="Lian Li O11 Air Mini", manufacturer="Lian Li", form_factor="Mid Tower",
                          color="White", msrp=110, ReleaseDate=date(2021, 12, 15))
            case87 = Case(case_name="Fractal Design Pop Air", manufacturer="Fractal Design", form_factor="Mid Tower",
                          color="Black", msrp=90, ReleaseDate=date(2022, 7, 12))
            case88 = Case(case_name="be quiet! Pure Base 700", manufacturer="be quiet!", form_factor="Mid Tower",
                          color="Black", msrp=110, ReleaseDate=date(2023, 9, 5))
            case89 = Case(case_name="Cooler Master TD300 Mesh", manufacturer="Cooler Master", form_factor="Mid Tower",
                          color="White", msrp=100, ReleaseDate=date(2021, 4, 20))
            case90 = Case(case_name="Thermaltake H350 TG", manufacturer="Thermaltake", form_factor="Mid Tower",
                          color="Black", msrp=80, ReleaseDate=date(2021, 6, 8))

            case91 = Case(case_name="NZXT H7", manufacturer="NZXT", form_factor="Mid Tower", color="White", msrp=130,
                          ReleaseDate=date(2022, 5, 17))
            case92 = Case(case_name="Corsair iCUE 7000X", manufacturer="Corsair", form_factor="Full Tower",
                          color="Black", msrp=330, ReleaseDate=date(2021, 5, 20))
            case93 = Case(case_name="Phanteks Eclipse P500A DRGB", manufacturer="Phanteks", form_factor="Mid Tower",
                          color="Black", msrp=130, ReleaseDate=date(2020, 7, 14))
            case94 = Case(case_name="Lian Li Q58", manufacturer="Lian Li", form_factor="Mini-ITX", color="White",
                          msrp=150, ReleaseDate=date(2021, 8, 11))
            case95 = Case(case_name="Fractal Design Torrent Compact", manufacturer="Fractal Design",
                          form_factor="Mid Tower", color="Black", msrp=140, ReleaseDate=date(2022, 2, 2))
            case96 = Case(case_name="be quiet! Shadow Rock 3", manufacturer="be quiet!", form_factor="Mid Tower",
                          color="Black", msrp=80, ReleaseDate=date(2020, 3, 10))
            case97 = Case(case_name="Cooler Master MasterBox NR200P MAX", manufacturer="Cooler Master",
                          form_factor="Mini-ITX", color="Black", msrp=350, ReleaseDate=date(2021, 9, 28))
            case98 = Case(case_name="Thermaltake The Tower 100", manufacturer="Thermaltake", form_factor="Mini-ITX",
                          color="Black", msrp=120, ReleaseDate=date(2020, 12, 22))
            case99 = Case(case_name="NZXT H9 Elite", manufacturer="NZXT", form_factor="Mid Tower", color="Black",
                          msrp=240, ReleaseDate=date(2023, 1, 17))
            case100 = Case(case_name="Corsair 2000D Airflow", manufacturer="Corsair", form_factor="Mid Tower",
                           color="Black", msrp=120, ReleaseDate=date(2023, 8, 1))

            case101 = Case(case_name="Phanteks Enthoo Pro 3", manufacturer="Phanteks", form_factor="Full Tower",
                           color="Black", msrp=170, ReleaseDate=date(2023, 10, 3))
            case102 = Case(case_name="Lian Li V3000 Plus", manufacturer="Lian Li", form_factor="Full Tower",
                           color="Silver", msrp=290, ReleaseDate=date(2023, 7, 11))
            case103 = Case(case_name="Fractal Design North XL", manufacturer="Fractal Design", form_factor="Mid Tower",
                           color="White", msrp=160, ReleaseDate=date(2023, 2, 7))
            case104 = Case(case_name="be quiet! Silent Base 802 Window", manufacturer="be quiet!",
                           form_factor="Mid Tower", color="White", msrp=180, ReleaseDate=date(2020, 11, 17))
            case105 = Case(case_name="Cooler Master HAF 700 EVO", manufacturer="Cooler Master",
                           form_factor="Full Tower", color="Black", msrp=400, ReleaseDate=date(2022, 3, 15))
            case106 = Case(case_name="Thermaltake Ceres 300 TG", manufacturer="Thermaltake", form_factor="Mid Tower",
                           color="Black", msrp=100, ReleaseDate=date(2023, 6, 13))
            case107 = Case(case_name="NZXT H6 Flow", manufacturer="NZXT", form_factor="Mid Tower", color="Black",
                           msrp=160, ReleaseDate=date(2024, 1, 16))
            case108 = Case(case_name="Corsair 3000D Airflow", manufacturer="Corsair", form_factor="Mid Tower",
                           color="White", msrp=135, ReleaseDate=date(2023, 10, 17))
            case109 = Case(case_name="Phanteks Revolt Pro", manufacturer="Phanteks", form_factor="Mini-ITX",
                           color="Black", msrp=140, ReleaseDate=date(2022, 10, 18))
            case110 = Case(case_name="Lian Li LANCOOL III", manufacturer="Lian Li", form_factor="Mid Tower",
                           color="Black/White", msrp=160, ReleaseDate=date(2022, 7, 19))

            case111 = Case(case_name="Fractal Design Meshify 2 XL", manufacturer="Fractal Design",
                           form_factor="Full Tower", color="Black", msrp=180, ReleaseDate=date(2020, 11, 24))
            case112 = Case(case_name="be quiet! Dark Base 900", manufacturer="be quiet!", form_factor="Full Tower",
                           color="Black/Orange", msrp=250, ReleaseDate=date(2021, 11, 9))
            case113 = Case(case_name="Cooler Master Cosmos C700M", manufacturer="Cooler Master",
                           form_factor="Full Tower", color="Black", msrp=440, ReleaseDate=date(2019, 10, 8))
            case114 = Case(case_name="Thermaltake Core P8", manufacturer="Thermaltake", form_factor="Full Tower",
                           color="Black", msrp=240, ReleaseDate=date(2020, 8, 11))
            case115 = Case(case_name="NZXT H6 Elite", manufacturer="NZXT", form_factor="Mid Tower", color="White",
                           msrp=190, ReleaseDate=date(2024, 1, 23))
            case116 = Case(case_name="Corsair 1000D", manufacturer="Corsair", form_factor="Super Tower", color="Black",
                           msrp=500, ReleaseDate=date(2019, 5, 9))
            case117 = Case(case_name="Phanteks Shift 2 Air", manufacturer="Phanteks", form_factor="Mini-ITX",
                           color="Black", msrp=100, ReleaseDate=date(2020, 12, 22))
            case118 = Case(case_name="Lian Li DAN Cases A4-H2O", manufacturer="Lian Li", form_factor="Mini-ITX",
                           color="Silver", msrp=130, ReleaseDate=date(2022, 2, 10))
            case119 = Case(case_name="Fractal Design Ridge", manufacturer="Fractal Design", form_factor="Mini-ITX",
                           color="Black", msrp=160, ReleaseDate=date(2023, 5, 23))
            case120 = Case(case_name="be quiet! Silent Base 803", manufacturer="be quiet!", form_factor="Mid Tower",
                           color="Black", msrp=190, ReleaseDate=date(2024, 3, 5))

            # Add all cases to database
            db.session.add_all([
                case1, case2, case3, case4, case5, case6, case7, case8, case9, case10,
                case11, case12, case13, case14, case15, case16, case17, case18, case19, case20,
                case21, case22, case23, case24, case25, case26, case27, case28, case29, case30,
                case31, case32, case33, case34, case35, case36, case37, case38, case39, case40,
                case41, case42, case43, case44, case45, case46, case47, case48, case49, case50,
                case51, case52, case53, case54, case55, case56, case57, case58, case59, case60,
                case61, case62, case63, case64, case65, case66, case67, case68, case69, case70,
                case71, case72, case73, case74, case75, case76, case77, case78, case79, case80,
                case81, case82, case83, case84, case85, case86, case87, case88, case89, case90,
                case91, case92, case93, case94, case95, case96, case97, case98, case99, case100,
                case101, case102, case103, case104, case105, case106, case107, case108, case109, case110,
                case111, case112, case113, case114, case115, case116, case117, case118, case119, case120
            ])

        # Add similar seed data for other models (Motherboard, Ram, Storage, Psu, Case, Build) as needed

        db.session.commit()
        print("Seed data inserted!")