
init -998 python:
    def enum(**enums):
        return type(str('Enum').encode( "ascii" ), (), enums)

init -998 python:
    Daytime = enum(morning='morning', afternoon='afternoon', evening='evening', night='night')

init offset = -990
define daytime = Daytime.morning
