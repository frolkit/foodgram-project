from rest_framework.response import Response
from rest_framework.views import APIView

from recipes.models import Recipe, Ingredient
from users.models import User, Purchase, Favorite, Subscribe


class PurchaseView(APIView):
    def post(self, request):
        recipe = Recipe.objects.get(id=request.data.get('id'))
        Purchase.objects.create(user=request.user, recipe=recipe)
        return Response({"ok": 'ok'})

    def delete(self, request, pk):
        recipe = Recipe.objects.get(id=pk)
        purchase_obj = Purchase.objects.get(recipe=recipe)
        purchase_obj.delete()
        return Response({"ok": 'ok'})


class FavoriteView(APIView):
    def post(self, request):
        recipe = Recipe.objects.get(id=request.data.get('id'))
        Favorite.objects.create(user=request.user, recipe=recipe)
        return Response({"ok": 'ok'})

    def delete(self, request, pk):
        recipe = Recipe.objects.get(id=pk)
        favorite_obj = Favorite.objects.get(recipe=recipe)
        favorite_obj.delete()
        return Response({"ok": 'ok'})


class SubscribeView(APIView):
    def post(self, request):
        following = User.objects.get(id=request.data.get('id'))
        print(following)
        print(request.user)
        Subscribe.objects.create(user=request.user, following=following)
        return Response({"ok": 'ok'})

    def delete(self, request, pk):
        following = User.objects.get(id=pk)
        subscribe_obj = Subscribe.objects.get(user=request.user, following=following)
        subscribe_obj.delete()
        return Response({"ok": "ok"})


class IngredientView(APIView):
    def get(self, request):
        item = self.request.query_params.get('query', None)
        ingredients = Ingredient.objects.filter(name__icontains=item).all()
        res = []
        for i in ingredients:
            res.append({"title": i.name, 'dimension': i.dimension})
        return Response(res)
