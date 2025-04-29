from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50),unique=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))
    builds = db.relationship('Build', backref='user', foreign_keys='Build.user_id')


class Gpu(db.Model):
    gpu_id = db.Column(db.Integer, primary_key=True)
    gpu_name = db.Column(db.String(50), nullable=False)
    manufacturer = db.Column(db.String(50), nullable=False)
    gpu_brand = db.Column(db.String(10), nullable=False)
    VRAM = db.Column(db.Integer, nullable=False)
    VRAM_type = db.Column(db.String(10), nullable=False)
    msrp = db.Column(db.Integer, nullable=False)
    PCIe = db.Column(db.Integer, nullable=False)
    ReleaseDate = db.Column(db.Date, nullable=False)


class Cpu(db.Model):
    cpu_id = db.Column(db.Integer, primary_key=True)
    cpu_name = db.Column(db.String(50), nullable=False)
    manufacturer = db.Column(db.String(50), nullable=False)
    cpu_brand = db.Column(db.String(10), nullable=False)
    cores = db.Column(db.Integer, nullable=False)
    threads = db.Column(db.Integer, nullable=False)
    base_clock = db.Column(db.Integer, nullable=False)
    boost_clock = db.Column(db.Integer, nullable=False)
    socket_type = db.Column(db.String(10), nullable=False)
    TDP = db.Column(db.Integer, nullable=False)
    msrp = db.Column(db.Integer, nullable=False)
    ReleaseDate = db.Column(db.Date, nullable=False)


class Motherboard(db.Model):
    motherboard_id = db.Column(db.Integer, primary_key=True)
    motherboard_name = db.Column(db.String(50), nullable=False)
    manufacturer = db.Column(db.String(50), nullable=False)
    socket_type = db.Column(db.String(20), nullable=False)
    chipset = db.Column(db.String(20), nullable=False)
    form_factor = db.Column(db.String(20), nullable=False)
    max_memory = db.Column(db.Integer, nullable=False)
    memory_slots = db.Column(db.Integer, nullable=False)
    max_memory_speed = db.Column(db.Integer, nullable=False)
    msrp = db.Column(db.Integer, nullable=False)
    ReleaseDate = db.Column(db.Date, nullable=False)


class Ram(db.Model):
    ram_id = db.Column(db.Integer, primary_key=True)
    ram_name = db.Column(db.String(50), nullable=False)
    manufacturer = db.Column(db.String(50), nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    ram_type = db.Column(db.String(10), nullable=False)
    speed = db.Column(db.Integer, nullable=False)
    msrp = db.Column(db.Integer, nullable=False)
    ReleaseDate = db.Column(db.Date, nullable=False)


class Storage(db.Model):
    storage_id = db.Column(db.Integer, primary_key=True)
    storage_name = db.Column(db.String(50), nullable=False)
    manufacturer = db.Column(db.String(50), nullable=False)
    storage_type = db.Column(db.String(10), nullable=False)
    capacity = db.Column(db.String(15), nullable=False)
    msrp = db.Column(db.Integer, nullable=False)
    speed = db.Column(db.String(15), nullable=False)
    ReleaseDate = db.Column(db.Date, nullable=False)


class Psu(db.Model):
    psu_id = db.Column(db.Integer, primary_key=True)
    psu_name = db.Column(db.String(50), nullable=False)
    manufacturer = db.Column(db.String(50), nullable=False)
    wattage = db.Column(db.Integer, nullable=False)
    efficiency_rating = db.Column(db.String(10), nullable=False)
    modular = db.Column(db.String(10), nullable=False)
    msrp = db.Column(db.Integer, nullable=False)
    ReleaseDate = db.Column(db.Date, nullable=False)


class Case(db.Model):
    case_id = db.Column(db.Integer, primary_key=True)
    case_name = db.Column(db.String(50), nullable=False)
    manufacturer = db.Column(db.String(50), nullable=False)
    form_factor = db.Column(db.String(30), nullable=False)
    color = db.Column(db.String(20), nullable=False)
    msrp = db.Column(db.Integer , nullable=False)
    ReleaseDate = db.Column(db.Date, nullable=False)


class Build(db.Model):
    BuildID = db.Column(db.Integer, primary_key=True)
    total_cost = db.Column(db.Integer, nullable=False)
    build_date = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    gpu_id = db.Column(db.Integer, db.ForeignKey('gpu.gpu_id'), nullable=False)
    cpu_id = db.Column(db.Integer, db.ForeignKey('cpu.cpu_id'), nullable=False)
    motherboard_id = db.Column(db.Integer, db.ForeignKey('motherboard.motherboard_id'), nullable=False)
    ram_id = db.Column(db.Integer, db.ForeignKey('ram.ram_id'), nullable=False)
    storage_id = db.Column(db.Integer, db.ForeignKey('storage.storage_id'), nullable=False)
    psu_id = db.Column(db.Integer, db.ForeignKey('psu.psu_id'), nullable=False)
    case_id = db.Column(db.Integer, db.ForeignKey('case.case_id'), nullable=False)
    gpu = db.relationship('Gpu')
    cpu = db.relationship('Cpu')
    motherboard = db.relationship('Motherboard')
    ram = db.relationship('Ram')
    storage = db.relationship('Storage')
    psu = db.relationship('Psu')
    case = db.relationship('Case')