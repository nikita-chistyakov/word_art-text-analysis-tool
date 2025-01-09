import input_manager
import processing
import output_manager

our_input = input_manager.read_csv()
our_result = processing(our_input)
output_manager(our_result)

