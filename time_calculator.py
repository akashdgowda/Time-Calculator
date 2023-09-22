def add_time(start, duration, dayOfWeek = False):
  daysOfTheWeekIndex = {"monday":0, "tuesday":1, "wednesday":2,     
  "thursday":3, "friday":4, "saturday":5, "sunday":6}

  daysOfTheWeekArray = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

  durationTuple = duration.partition(":")
  #Example for partition: ('2',':','50')
  durationHours = int(durationTuple[0])
  durationMinutes = int(durationTuple[2])
  
  startTuple = start.partition(":")
  startMinuteTuple = startTuple[2].partition(" ")
  #example: startTuple = {'3',':','45 AM'}
  # startMinuteTuple = {'45',' ', 'AM'}
  startHours = int(startTuple[0])
  startMinutes = int(startMinuteTuple[0])
  AMorPM = startMinuteTuple[2]
  AMandPMFlip = {"AM" : "PM", "PM":"AM"}

  amountOfDays = int(durationHours / 24)

  endMinutes = startMinutes + durationMinutes
  if(endMinutes >= 60):
    startHours += 1
    endMinutes = endMinutes % 60
  amountOfAMPMFlips = int((startHours + durationHours)/12)
  endHours = (startHours + durationHours) % 12

  endMinutes = endMinutes if endMinutes > 9 else "0" + str(endMinutes)
  endHours = endHours =12 if endHours == 0 else endHours

  if(AMorPM == "PM" and startHours + (durationHours%12) >= 12 ):
    amountOfDays += 1
  
  


  AMorPM = AMandPMFlip[AMorPM] if amountOfAMPMFlips%2 ==1 else AMorPM

  returnTime = str(endHours) + ":" + str(endMinutes) + " " + AMorPM

  if(dayOfWeek):
    dayOfWeek = dayOfWeek.lower()
    index = int((daysOfTheWeekIndex[dayOfWeek]) + amountOfDays) % 7
    newDay = daysOfTheWeekArray[index]
    returnTime += ", " + newDay

  if(amountOfDays == 1):
    return returnTime + " " + "(next day)"
  elif(amountOfDays > 1):
    return returnTime + " (" + str(amountOfDays) + " days later)"
    


  return returnTime