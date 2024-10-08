from app import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash



class Chamado(db.Model):
    """Tabela de chamados"""
    __tablename__ = "calls"
    id = db.Column(db.Integer, primary_key=True)
    Object_id = db.Column(db.Integer, db.ForeignKey('object.id'), nullable=False)
    Problem = db.Column(db.String(60))
    Description = db.Column(db.String(400))
    Status = db.Column(db.String(60))
    Time_created = db.Column(db.Date)
    User_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)

    def __init__(self, params):
        self.Object_id = params.get('Object_id')
        self.Problem = params.get('Problem')
        self.Description = params.get('Description')
        self.Status = params.get('Status')
        self.Time_created = params.get('Time_created')
        self.User_id = int(params.get('User_id'))



#Login Stuff
@login_manager.user_loader
def get_user(user_id):
    return User.query.filter_by(id=user_id).first()


class User(db.Model, UserMixin):
    """Tabela de Usuarios"""
    __tablename__ = 'users'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(200),nullable=False)
    email = db.Column(db.String(120),nullable=False, unique=True)
    password_hash = db.Column(db.String(300), nullable=False)
    chamados = db.relationship('Chamado', backref='users')


    @property
    def password(self):
        raise AttributeError ('password is not a readable attribute!')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


class Object(db.Model):
    """Tabela de Object"""
    __tablename__ = 'object'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    Object_lab = db.Column(db.String(45))
    Object_div= db.Column(db.String(300))
    Object_compname = db.Column(db.String(45))
    Object_comp_processor = db.Column(db.String(45))
    Object_comp_RAM = db.Column(db.String(45))
    Object_comp_operational_system = db.Column(db.String(45))
    computer = db.relationship('Chamado', backref='object')

    def __init__(self, params):
        self.Object_lab = params.get('Object_lab')
        self.Object_div= params.get('Object_div')
        self.Object_compname = params.get('Object_compname')
        self.Object_comp_processor = params.get('Object_comp_processor')
        self.Object_comp_RAM = params.get('Object_comp_RAM')
        self.Object_comp_operational_system = params.get('Object_comp_operational_system')
