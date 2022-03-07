from dataclasses import field
from rest_framework import serializers
from .models import Matrix, String


class MatrixNormalSerializer(serializers.ModelSerializer):

    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault())

    class Meta:
        model = Matrix
        fields = ['user', 'matrix', 'output_data']

    def validate(self, data):
        if not isinstance(data['matrix'], list):  # Matrix as List
            raise serializers.ValidationError("Input matrix should be a list")

        if not len(data['matrix']):  # Not empty list
            raise serializers.ValidationError("Input matrix is empty")

        return data



class MatrixDiagonallSerializer(serializers.ModelSerializer):

    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault())

    class Meta:
        model = Matrix
        fields = ['user', 'matrix', 'output_data']

    def validate(self, data):
        if not isinstance(data['matrix'], list):  # Matrix as List
            raise serializers.ValidationError("Input matrix should be a list")

        if not len(data['matrix']):  # Not empty list
            raise serializers.ValidationError("Input matrix is empty")

        if any( len(row) != len(data['matrix']) for row in data['matrix'] ): # Square matrix
            raise serializers.ValidationError("Input matrix is not square")

        return data



class StringEncoderSerializer(serializers.ModelSerializer):

    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault())

    class Meta:
        model = String
        fields = ['user', 'string', 'output_data']