from flask import Blueprint, request, jsonify
from pydantic import ValidationError
from .models import subscription, Subscription
from .auth import authenticate_request
from .utils import calculate_end_date
from datetime import datetime

api = Blueprint('api', __name__)


@api.route('/subscription', methods=['POST'])
@authenticate_request
def create_subscription():
    try:
        data = request.json

        if 'start_date' in data and isinstance(data['start_date'], str):
            try:
                data['start_date'] = datetime.strptime(data['start_date'], '%Y-%m-%d')
            except ValueError as ve:
                return jsonify({'error': 'start_date must be in the format YYYY-MM-DD'}), 422

        subscription = Subscription(**data)
        if subscription.start_date:
            subscription.end_date = calculate_end_date(subscription.start_date, subscription.duration)
        subscription.save()
        return jsonify({'message': 'Subscription created', 'subscription_id': subscription.user_external_id}), 201
    except ValidationError as e:
        return jsonify({'error': e.errors()}), 422
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@api.route('/subscription', methods=['PUT'])
@authenticate_request
def extend_subscription():
    try:
        data = request.json
        user_external_id = data.get('user_external_id')
        duration = int(data.get('duration'))
        current_subscription = subscription.get(user_external_id)

        if not current_subscription:
            return jsonify({'error': 'Subscription not found'}), 404

        current_subscription.end_date = calculate_end_date(current_subscription.end_date, duration)
        current_subscription.save()
        return jsonify({'message': 'Subscription extended',
                        'new_end_date': current_subscription.end_date.strftime('%Y-%m-%d')}), 200
    except ValidationError as e:
        return jsonify({'error': e.errors()}), 422
    except Exception as e:
        return jsonify({'error': str(e)}), 400
