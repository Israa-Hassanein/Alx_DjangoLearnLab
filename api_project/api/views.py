from rest_framework import viewsets
from .models import Book
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import BookSerializer
from .permissions import IsCreatorOrAdmin

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsCreatorOrAdmin] 


    # You can also define different permissions for different actions
    # For example, only admin users can delete books:
    def perform_destroy(self, instance):
        if not self.request.user.is_staff:
            raise PermissionDenied("You do not have permission to delete this book.")
        instance.delete()

