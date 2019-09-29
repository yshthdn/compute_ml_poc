from flask import make_response, abort
from models import Config, ConfigSchema, ComputeForecastResponse, ComputeForecastResponseSchema
from config import db
from predict import predict_confidence, get_rule_id


def create(body):
    print(body)
    # import ipdb;ipdb.set_trace()
    schema = ConfigSchema()
    job_id = body.get("job_id")
    project_id = body.get("project_id")
    existing_config = (
        Config.query.filter(Config.job_id == job_id)
            .filter(Config.project_id == project_id)
            .one_or_none()
    )
    if existing_config is None:

        new_config = schema.load(body, session=db.session)
        # Add the config to the database
        db.session.add(new_config)
        db.session.commit()
        data = schema.dump(new_config)

        return data, 201
        # return make_response(
        #     "Success", 201
        # )
    else:
        abort(
            409,
            "Config {job_id} {project_id} exists already".format(
                job_id=job_id, project_id=project_id
            ),
        )


def read_all():
    # Create the list of people from our data
    config = Config.query.order_by(Config.job_id).all()

    # Serialize the data for the response
    config_schema = ConfigSchema(many=True)
    data = config_schema.dump(config)
    return data


def read_one(job_id):
    config = (
        Config.query.filter(Config.job_id == job_id)
            .one_or_none()
    )
    schema = ConfigSchema()
    if config is None:
        abort(
            404,
            "Config not found for Id: {job_id}".format(job_id=job_id),
        )
    else:
        data = schema.dump(config)
        return data, 200


def update(body):
    """
    This function updates an existing person in the people structure
    Throws an error if a person with the name we want to update to
    already exists in the database.

    :param person_id:   Id of the person to update in the people structure
    :param person:      person to update
    :return:            updated person structure
    """
    job_id = body.get("job_id")
    project_id = body.get("project_id")
    update_config = Config.query.filter(
        Config.job_id == job_id
    ).one_or_none()

    existing_config = (
        Config.query.filter(Config.job_id == job_id)
            .filter(Config.project_id == project_id)
            .one_or_none()
    )

    # Are we trying to find a config that does not exist?
    if update_config is None:
        abort(
            404,
            "Config not found for Id: {job_id}".format(job_id=job_id),
        )

    # Would our update create a duplicate of another config already existing?
    elif (
        existing_config is not None and existing_config.job_id != job_id
    ):
        abort(
            409,
            "Config {job_id} {project_id} exists already".format(
                job_id=job_id, project_id=project_id
            ),
        )

    # Otherwise go ahead and update!
    else:

        # turn the passed in person into a db object
        schema = ConfigSchema()
        update = schema.load(body, session=db.session)

        # Set the id to the person we want to update
        update.job_id = update_config.job_id

        # merge the new object into the old and commit it to the db
        db.session.merge(update)
        db.session.commit()

        # return updated person in the response
        data = schema.dump(update_config)

        return data, 200


def delete(job_id):
    """
    This function deletes a config from the config structure

    :param job_id:   Id of the job to delete
    :return:            200 on successful delete, 404 if not found
    """
    # Get the person requested
    config = Config.query.filter(Config.job_id == job_id).one_or_none()

    # Did we find a person?
    if config is not None:
        db.session.delete(config)
        db.session.commit()
        return make_response(
            "Config {job_id} deleted".format(job_id=job_id), 200
        )

    # Otherwise, nope, didn't find that person
    else:
        abort(
            404,
            "Config not found for Id: {job_id}".format(job_id=job_id),
        )


def predict(job_id):
    config = (
        Config.query.filter(Config.job_id == job_id)
            .one_or_none()
    )


    if config:
        #predict
        model_id = config.model_id
        response = (
            ComputeForecastResponse.query.filter(ComputeForecastResponse.model_id == model_id)
                .one_or_none()
        )
        response_schema = ComputeForecastResponseSchema()
        if response is None:
            response = ComputeForecastResponse()

            response.cpu_request = config.cpu_request
            response.time_request = config.time_request
            response.project_id = config.project_id
            response.project_desc = config.project_desc
            response.project_phase = config.project_phase
            response.design_block_id = config.design_block_id
            response.design_block_desc = config.design_block_desc
            response.tool_used = config.tool_used
            response.tool_cmd = config.tool_cmd
            response.mem_request = config.mem_request
            response.tool_used = config.tool_used
            response.confidence_score = str(predict_confidence(model_id))
            response.model_id = model_id
            response.rule_id = get_rule_id(model_id)

            db.session.add(response)
            db.session.commit()
        # import ipdb;ipdb.set_trace()
        data = response_schema.dump(response)

        return data, 200

    else:
        abort(
            404,
            "Config not found for Id: {job_id}".format(job_id=job_id),
        )

