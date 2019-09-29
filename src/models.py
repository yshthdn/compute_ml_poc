import enum
from datetime import datetime
from config import db, ma
from sqlalchemy import Enum
from sqlalchemy.schema import PrimaryKeyConstraint


class ConfidenceLevel(enum.Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3


class Config(db.Model):
    __tablename__ = 'JOB_RESOURCE_USAGE'
    job_id = db.Column(db.Integer, primary_key=True)
    mem_request = db.Column(db.String(32))
    cpu_request = db.Column(db.String(32))
    # time_request = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    time_request = db.Column(db.String(32))
    project_id = db.Column(db.String(32), primary_key=True)
    project_desc = db.Column(db.String(32))
    project_phase = db.Column(db.String(32))
    design_block_id = db.Column(db.String(32))
    design_block_desc = db.Column(db.String(32))
    tool_used = db.Column(db.String(32))
    tool_cmd = db.Column(db.String(32))
    model_id = db.Column(db.String(32))
    __table_args__ = (
        PrimaryKeyConstraint(
            job_id,
            project_id),
        {})


class ComputeForecastResponse(db.Model):
    __tablename__ = 'JOB_RESOURCE_PREDICTION'
    model_id = db.Column(db.Integer, primary_key=True)
    rule_id = db.Column(db.Integer, primary_key=True)
    mem_request = db.Column(db.String(32))
    cpu_request = db.Column(db.String(32))
    # time_request = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    time_request = db.Column(db.String(32))
    project_id = db.Column(db.String(32))
    project_desc = db.Column(db.String(32))
    project_phase = db.Column(db.String(32))
    design_block_id = db.Column(db.String(32))
    design_block_desc = db.Column(db.String(32))
    tool_used = db.Column(db.String(32))
    tool_cmd = db.Column(db.String(32))
    confidence_score = db.Column(db.String(32))

    __table_args__ = (
        PrimaryKeyConstraint(
            model_id,
            rule_id),
        {})


class ConfigSchema(ma.ModelSchema):
    class Meta:
        model = Config
        sqla_session = db.session


class ComputeForecastResponseSchema(ma.ModelSchema):
    class Meta:
        model = ComputeForecastResponse
        sqla_session = db.session



