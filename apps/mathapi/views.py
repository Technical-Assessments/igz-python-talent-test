from django.contrib.auth import authenticate
from urllib.request import Request
from django.shortcuts import redirect, render
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import (
    MatrixNormalSerializer,
    MatrixDiagonallSerializer,
    StringEncoderSerializer
)
from .models import Matrix
from .utils.matrix import (
    elements_sum,
    diagonal_sum
)
from .utils.compression import encode


# Normal Sum of matrix elements
@api_view(['POST'])
@permission_classes([AllowAny])
def matrix_sum_view(request: Request) -> Response:
    """ This service returns the sum of all the elements of a given matrix.
        But it is important to introduce the matrix in JSON format.

        For example:

                    {"matrix": [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ] }
    """

    if not request.user.username:
        return redirect("/api-auth/login/?next=/api/matrix/sum/")

    # Serialize request object
    serializer = MatrixNormalSerializer(
        data=request.data,
        # Request as context so the serializer can extract the current user field.
        context={'request': request}
    )

    # Validate serializer format
    if serializer.is_valid(raise_exception=True):
        serializer.save(
            # Save the request data including the output data & type fields
            output_data=elements_sum(request.data['matrix']),
            output_type="N"
        )

    return Response(
        {
            "Input matrix": serializer.data['matrix'],
            "Sum of all elements": serializer.data['output_data']
        }
    )



# Diagonal sum of matrix elements
@api_view(['POST'])
def matrix_diagonal_sum_view(request: Request) -> Response:
    """ This service returns the sum of all the elements of the given matrix main diagonal.
        But it is important to introduce the matrix in JSON format.

        For example: {"matrix": [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ] }

        In this case, if the matrix is not squared (inner lists of numbers are not equal length)
        an error will be prompted
        
    """
    if not request.user.username:
        return redirect("/api-auth/login/?next=/api/matrix/diagonal_sum/")

    # Serialize request object
    serializer = MatrixDiagonallSerializer(
        data=request.data,
        # Request as context so the serializer can extract the current user field.
        context={'request': request}
    )

    # Validate serializer format
    if serializer.is_valid(raise_exception=True):
        serializer.save(
            # Save the request data including the output data & type fields
            output_data=diagonal_sum(request.data['matrix']),
            output_type="D"
        )

    return Response(
        {
            "Input matrix": serializer.data['matrix'],
            "Sum of elements in main diagonal": serializer.data['output_data']
        }
    )



# String encoer
@api_view(['POST'])
def string_encoder_view(request: Request) -> Response:
    """
        This tool will provide you an almost-decent safe way to encode your secret password.

        Type the password to encode in the following format: { "string": "aaAabaccCBb" }
    """

    if not request.user.username:
        return redirect("/api-auth/login/?next=/api/string/encode/")

    # Serialize request object
    serializer = StringEncoderSerializer(
        data=request.data,
        # Request as context so the serializer can extract the current user field.
        context={'request': request}
    )

    # Validate serializer format
    if serializer.is_valid(raise_exception=True):
        serializer.save(
            output_data=encode(request.data['string'])
        )

    return Response(
        {
            "Input string": serializer.data['string'],
            "Encoded string": serializer.data['output_data']
        }
    )



# Viewset approach
""" # POST: /api/matrix/sum
    class MatrixSumView(APIView):

        def get(self, request):
            data = Matrix.objects.all()
            serializer = MatrixNormalSerializer(data, many=True)
            return Response(serializer.data)


        def post(self, request):
            serializer = MatrixNormalSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)


    # POST: /api/matrix/diagonal_sum
    class DiagonalMatrixSumView(APIView):

        def post(self, request):
            return


    # POST: /api/string/encode
    class StringEncoderView(APIView):

        def post(self, request):
            return
         """


""" # POST: /api/matrix/sum
class MatrixSumView(
    viewsets.ViewSet,
    viewsets.ModelViewSet
):

    queryset = Matrix.objects.all()
    serializer_class = MatrixNormalSerializer
    permission_classes = [permissions.IsAdminUser]
    http_method_names = ['get', 'post']


    def create(self, request):
        serializer = MatrixNormalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data) """
