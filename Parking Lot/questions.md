[Question Link](https://workat.tech/machine-coding/practice/design-parking-lot-qm6hwq4wkhp8)

Requirements
Create a command-line application for the parking lot system with the following requirements.

The functions that the parking lot system can do:
<ul>
  <li>Create the parking lot.</li>
  <li>Add floors to the parking lot.</li>
 <li> Add a parking lot slot to any of the floors.</li>
  <li>Given a vehicle, it finds the first available slot, books it, creates a ticket, parks the vehicle, and finally returns the ticket.</li>
  <li>Unparks a vehicle given the ticket id.</li>
 <li> Displays the number of free slots per floor for a specific vehicle type.</li>
  <li>Displays all the free slots per floor for a specific vehicle type.</li>
  <li>Displays all the occupied slots per floor for a specific vehicle type.</li>
</ul>


Details about the Vehicles:
<ul>
 <li>  Every vehicle will have a type, registration number, and color. </li>
    Different Types of Vehicles:
     <li>Car </li>
    <li> Bike </li>
   <li>  Truck </li>
</ul>

Details about the Parking Slots:
<ul>
 <li> Each type of slot can park a specific type of vehicle.</li>
 <li> No other vehicle should be allowed by the system.</li>
 <li> Finding the first available slot should be based on:</li>
  <ul>
    <li>The slot should be of the same type as the vehicle.</li>
   <li> The slot should be on the lowest possible floor in the parking lot.</li>
   <li> The slot should have the lowest possible slot number on the floor.</li>
  </ul>
  Numbered serially from 1 to n for each floor where n is the number of parking slots on that floor.
</ul>


Details about the Parking Lot Floors:
<ul>
<li>Numbered serially from 1 to n where n is the number of floors.</li>
<li>Might contain one or more parking lot slots of different types.</li>
<li>We will assume that the first slot on each floor will be for a truck, the next 2 for bikes, and all the other slots for cars.</li>
</ul>

Details about the Tickets:
<li>The ticket id would be of the following format:</li>
<parking_lot_id>_<floor_no>_<slot_no>
<li>Example: PR1234_2_5 (denotes 5th slot of 2nd floor of parking lot PR1234)</li>

We can assume that there will only be 1 parking lot. The ID of that parking lot is PR1234.




