# -*- coding: utf-8 -*-

from .. import db

class School(db.Model):
    __tablename__ = 'school'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'), nullable=False)
    admin = db.relationship('Admin', backref=db.backref('schools', lazy='dynamic'))
    def __repr_(self):
        return '<School %d %s>' % (self.id, self.name)

class Building(db.Model):
    __tablename__ = 'building'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    school_id = db.Column(db.Integer, db.ForeignKey('school.id'), nullable=False)
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'), nullable=False)
    school = db.relationship('School', backref=db.backref('buildings', lazy='dynamic'))
    admin = db.relationship('Building', backref=db.backref('buildings', lazy='dynamic'))
    def __repr_(self):
        return '<Building %d %s>' % (self.id, self.name)

