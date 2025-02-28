#in this program I am doing the filtering of the data based on the condition
#In that I am creating the list and applying the filter on the data based on the duration of the plant
import apache_beam as beam

def is_perennial(plant):
  return plant['duration'] == '4 months'

with beam.Pipeline() as p:
  perennials = (
      p | 'Gardening plants' >> beam.Create([
          {
              'icon': '🍓', 'name': 'Strawberry', 'duration': '5 months'
          },
          {
              'icon': '🥕', 'name': 'Carrot', 'duration': '3 months'
          },
          {
              'icon': '🍆', 'name': 'Eggplant', 'duration': '4 months'
          },
          {
              'icon': '🍅', 'name': 'Tomato', 'duration': '4 months'
          },
          {
              'icon': '🥔', 'name': 'Potato', 'duration': '4 months'
          },
      ])
      | 'Filter perennials' >> beam.Filter(is_perennial)
      | beam.Map(print)) 