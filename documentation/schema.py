import graphene
from graphene_django import DjangoObjectType

# from graphql import language # This import is unnecessary and can be removed
from .models import Languague


# --- 1. Types ---


class LanguagueType(DjangoObjectType):
    # GraphQL Type definition for the Languague Model
    class Meta:
        model = Languague
        fields = '__all__'


# --- 2. Query: Data Fetching ---


class Query(graphene.ObjectType):
    # Field to list all Languague objects
    all_languagues = graphene.List(LanguagueType)

    # Field to fetch a single Languague by ID
    id = graphene.ID(required=True)
    languague_with_id = graphene.Field(LanguagueType, id=id)

    # Resolver for fetching all languages
    def resolve_all_languagues(self, info):
        return Languague.objects.all()

    # Resolver for fetching a single language by ID
    def resolve_languague_with_id(self, info, id):
        try:
            return Languague.objects.get(id=id)
        except Languague.DoesNotExist:
            return None


# --- 3. Mutations: CUD Operations ---


class CreateLanguague(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)

    language = graphene.Field(LanguagueType)

    # Use @classmethod decorator for mutate
    @classmethod
    def mutate(cls, root, info, name):
        language = Languague(name=name)
        language.save()
        return CreateLanguague(language=language)


class UpdateLanguague(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String(required=True)

    language = graphene.Field(LanguagueType)

    # Use @classmethod decorator for mutate
    @classmethod
    def mutate(cls, root, info, id, name):
        try:
            language = Languague.objects.get(id=id)
        except Languague.DoesNotExist:
            raise Exception(f"Languague with ID {id} not found.")

        language.name = name
        language.save()
        return UpdateLanguague(language=language)


class DeleteLanguage(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    # Return a Boolean for success status instead of the deleted object
    success = graphene.Boolean()

    # Use @classmethod decorator for mutate
    @classmethod
    def mutate(cls, root, info, id):
        try:
            language = Languague.objects.get(id=id)
        except Languague.DoesNotExist:
            raise Exception(f"Languague with ID {id} not found.")

        language.delete()
        # Return success status
        return DeleteLanguage(success=True)


# --- 4. Root Mutation Class ---


class Mutation(graphene.ObjectType):
    create_languague = CreateLanguague.Field()
    update_languague = UpdateLanguague.Field()
    delete_language = DeleteLanguage.Field()


# --- 5. Root Schema Definition (Linking with settings) ---

schema = graphene.Schema(query=Query, mutation=Mutation)
