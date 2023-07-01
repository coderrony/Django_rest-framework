from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatform, Review


class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        # fields = "__all__"
        exclude = ('watchlist',)


class MovieSerializer(serializers.ModelSerializer):
    len_name = serializers.SerializerMethodField()
    review = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = WatchList
        fields = "__all__"
        # exclude = ['active']

    def get_len_name(self, object):
        return len(object.title)


class StreamPlatformSerializer(serializers.ModelSerializer):
    watch_list = MovieSerializer(many=True, read_only=True)

    # watch_list = serializers.StringRelatedField(many=True)
    # watch_list = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='movie_details'
    # )  #context={'request': request}
    # watch_list = serializers.SlugRelatedField(
    #     many=True,
    #     read_only=True,
    #     slug_field='storyline'
    # )

    class Meta:
        model = StreamPlatform
        fields = "__all__"

    # def validate(self, data):
    #     if data['name'] == data['description']:
    #         raise serializers.ValidationError(
    #             "name and description should be different")
    #     else:
    #         return data

    # def validate_name(self, value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError("to short")
    #     else:
    #         return value


# def name_length(value):
#     if len(value) < 2:
#         raise serializers.ValidationError("Name is to short!")

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()

#     def create(self, validate_date):
#         return Movie.objects.create(**validate_date)

#     def update(self, instance, validate_data):
#         instance.name = validate_data.get('name', instance.name)
#         instance.description = validate_data.get(
#             'description', instance.description)
#         instance.active = validate_data.get('active', instance.active)
#         instance.save()
#         return instance

# # file level validation
#     # def validate_name(self, value):
#     #     if len(value) < 2:
#     #         raise serializers.ValidationError("Name is to short!")
#     #     else:
#     #         return value

# # Object Level Validation
#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError(
#                 "name and description must be different")
#         else:
#             return data
