# Bugs
- adjust raise error when StarDeck is as deck defined and rails is bigger then 55 "Rails must be between 1 and 55")
- row ~158 num rails is 54 not 55:
return HamiltonDeck(
      num_rails=55,<----
      size_x=1900,
      size_y=653.5,
      size_z=900,
      resource_assigned_callback=resource_assigned_callback,
      resource_unassigned_callback=resource_unassigned_callback,
      origin=origin)

# Features 
- a fake connection, so that I dont need to be connected to usb for testing some things
