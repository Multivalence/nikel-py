from nikel_py.utils._constants import *
from nikel_py.utils.errors import InvalidKey


# #Currently not being used but better support may be added in the future
# OPERATORS = ("!", "<", "<=", ">", ">=", "(", ")", "~")


def url_parse(base_url : str, query : dict, limit : int) -> str:

    lookup = {
        COURSES_BASE_URL : ('id', 'code', 'name', 'description', 'division', 'department', 'prerequisites', 'corequisites', 'exclusions', 'recommended_preparation', 'level', 'campus', 'term', 'arts_and_science_breadth', 'arts_and_science_distribution', 'utm_distribution', 'utsc_breadth', 'apsc_electives', 'meeting_sections', 'last_updated'),
        PROGRAMS_BASE_URL : ('id', 'name', 'type', 'campus', 'description', 'enrollment', 'completion', 'last_updated'),
        TEXTBOOKS_BASE_URL : ('id', 'isbn', 'title', 'edition', 'author', 'image', 'price', 'url', 'courses', 'last_updated'),
        EXAMS_BASE_URL : ('id', 'course_id', 'course_code', 'campus', 'date', 'start', 'end', 'duration', 'sections', 'last_updated'),
        EVALS_BASE_URL : ('id', 'name', 'campus', 'terms', 'last_updated'),
        FOOD_BASE_URL : ('id', 'name', 'description', 'tags', 'campus', 'address', 'coordinates', 'hours', 'image', 'url', 'twitter', 'facebook', 'attributes', 'last_updated'),
        SERVICES_BASE_URL : ('id', 'name', 'alias', 'building_id', 'description', 'campus', 'address', 'image', 'coordinates', 'tags', 'attributes', 'last_updated'),
        BUILDINGS_BASE_URL : ('id', 'code', 'tags', 'name', 'short_name', 'address', 'coordinates', 'last_updated'),
        PARKING_BASE_URL : ('id', 'name', 'alias', 'building_id', 'description', 'campus', 'address', 'coordinates', 'last_updated')
    }

    for i in query:

        if i not in lookup[base_url[:base_url.find("?") + 1]]:
            raise InvalidKey(i)

        if isinstance(query[i], str):

            if " " in query[i]:

                if query[i].startswith("~"):
                    query[i] = query[i].replace(" ", f"&{i}=~")

                else:
                    query[i] = query[i].replace(" ", f"&{i}=")



        base_url += f"&{i}={query[i]}"

    base_url += f"&limit={limit}" if (limit >=1 and limit <=100) else "&limit=100"

    return base_url