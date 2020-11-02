from django import template

from users.models import Purchase, Favorite, Subscribe


register = template.Library()


@register.filter
def addclass(field, css):
    return field.as_widget(attrs={"class": css})


@register.filter()
def check_favorite(recipe, user):
    favorite = Favorite.objects.filter(user=user.id, recipe=recipe.id).exists()
    return favorite


@register.filter()
def check_purchase(recipe, user):
    purchase = Purchase.objects.filter(user=user.id, recipe=recipe.id).exists()
    return purchase


@register.filter()
def check_subcribe(user, following):
    subscribe = Subscribe.objects.filter(
        user=user.id, following=following.id).exists()
    return subscribe


@register.simple_tag(takes_context=True)
def get_purchases(context, **kwargs):
    request = context['request']
    purchases = Purchase.objects.filter(user=request.user).all()
    return len(purchases)


@register.simple_tag(takes_context=True)
def tagcolor(context, **kwargs):
    classes = {
        'breakfast': 'badge badge_style_green',
        'lunch': 'badge badge_style_orange',
        'dinner': 'badge badge_style_purple'
    }
    tag = kwargs['tag']
    color_class = classes[tag]
    return color_class


@register.simple_tag(takes_context=True)
def generate_filter_url(context, **kwargs):
    query = context['request'].GET.copy()
    tag_current = kwargs['tag']
    tags_active = query.getlist('tag')
    if tag_current in tags_active:
        tags_active = query.pop('tag')
        tags_active.remove(tag_current)
        for tag in tags_active:
            query.appendlist('tag', tag)
    else:
        query.appendlist('tag', tag_current)
    return query.urlencode()


@register.simple_tag(takes_context=True)
def generate_page_url(context, **kwargs):
    query = context['request'].GET.copy()
    for k, v in kwargs.items():
        query[k] = v
    for k in [k for k, v in query.items() if not v]:
        del query[k]
    return query.urlencode()
