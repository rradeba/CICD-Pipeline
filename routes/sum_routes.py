from flask import Blueprint, jsonify
from sqlalchemy.exc import SQLAlchemyError
from models.sum import Sum
from schemas.sum_schema import sums_schema

sum_bp = Blueprint('sum_bp', __name__)

@sum_bp.route('/sum/result/<int:result_value>', methods=['GET'])
def get_sums_by_result(result_value):
    try:
        sums = Sum.query.filter_by(result=result_value).all()
        sums_data = sums_schema.dump(sums)
        return jsonify(sums_data), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500
