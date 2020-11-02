from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from recipes.models import Recipe, Ingredient
from users.models import User, Purchase, Favorite, Subscribe


class PurchaseView(APIView):
    def post(self, request):
        recipe = get_object_or_404(Recipe, id=request.data.get('id'))
        obj, created = Purchase.objects.get_or_create(user=request.user,
                                                      recipe=recipe)
        if created:
            return Response({'status': '201'})
        return Response({"status": '302'})

    def delete(self, request, pk):
        recipe = get_object_or_404(Recipe, id=pk)
        purchase_obj = get_object_or_404(Purchase, user=request.user,
                                         recipe=recipe)
        purchase_obj.delete()
        return Response({"status": '204'})


class FavoriteView(APIView):
    def post(self, request):
        recipe = get_object_or_404(Recipe, id=request.data.get('id'))
        obj, created = Favorite.objects.get_or_create(user=request.user,
                                                      recipe=recipe)
        if created:
            return Response({'status': '201'})
        return Response({"status": '302'})

    def delete(self, request, pk):
        recipe = get_object_or_404(Recipe, id=pk)
        favorite_obj = get_object_or_404(Favorite, user=request.user,
                                         recipe=recipe)
        favorite_obj.delete()
        return Response({"status": '204'})


class SubscribeView(APIView):
    def post(self, request):
        following = get_object_or_404(User, id=request.data.get('id'))
        obj, created = Subscribe.objects.get_or_create(user=request.user,
                                                       following=following)
        if created:
            return Response({'status': '201'})
        return Response({"status": '302'})

    def delete(self, request, pk):
        following = get_object_or_404(User, id=pk)
        subscribe_obj = get_object_or_404(Subscribe, user=request.user,
                                          following=following)
        subscribe_obj.delete()
        return Response({"status": '204'})


class IngredientView(APIView):
    def get(self, request):
        item = self.request.query_params.get('query', None).lower()
        ingredients = Ingredient.objects.filter(
            title__icontains=item).values('title', 'dimension')
        return Response(ingredients)
