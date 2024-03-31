from enum import Enum 

class VehicleType(Enum):
	TRUCK, BIKE, CAR = 0, 1, 2 

class SlotStatus(Enum):
	AVAILABLE, OCCUPIED = 0, 1 


class Vehicle :
	def __init__(self, vehicle_type, reg_num, color):
		self.vehicle_type = vehicle_type
		self.reg_num = reg_num
		self.color = color 

	def __str__(self):
		return "Vehicle Reg_num : {}, Vehicle Type: {}, Vehicle Color : {}".format(self.reg_num, self.vehicle_type.name, self.color)

class ParkingSlot:
	def __init__(self, vehicle_type, slot_num, floor_num, slot_status = SlotStatus.AVAILABLE, vehicle = None):
		self.vehicle_type = vehicle_type
		self.slot_num = slot_num
		self.floor_num = floor_num
		self.vehicle = vehicle
		self.slot_status = slot_status

	def __str__(self):
		summary = {
			"vehicle_type" : self.vehicle_type.name,
			"slot_num" : self.slot_num ,
			"floor_num" : self.floor_num ,
			"vehicle" : str(self.vehicle) ,
			"slot_status" :  self.slot_status.name
		}
		return str(summary)

	def can_be_added(self):
		return self.slot_status == SlotStatus.AVAILABLE

	def add_vehicle(self, new_vehicle):
		if new_vehicle.vehicle_type != self.vehicle_type :
			return "Cannot add vehicle due to mismatching vehicle type, can only add vehicle of type : " + self.vehicle_type.name

		if not self.can_be_added():
			return "Slot capacity reached"

		self.vehicle = new_vehicle
		self.slot_status = SlotStatus.OCCUPIED
		return "Successfully added vehicle : {}".format(str(new_vehicle))

	def display_all_vehicles(self):
		for vehicle in self.vehicles :
			print(vehicle)

	def remove_vehicle(self):
		if self.slot_status == SlotStatus.AVAILABLE :
			return "Slot already empty"
		vehicle = self.vehicle
		self.vehicle = None
		self.slot_status = SlotStatus.AVAILABLE
		return "Successfully removed vehicle from parking slot: {}".format(str(vehicle))

	def is_available(self):
		return self.slot_status == SlotStatus.AVAILABLE


class ParkingFloor:
	def __init__(self, floor_num, floor_size, parking_slots = []):
		self.floor_num = floor_num
		self.parking_slots = parking_slots
		self.floor_size = floor_size 

	def __str__(self):
		summary = {
			"floor_num" : self.floor_num,
			"floor_size" : self.floor_size,
			"parking_slots" : self.parking_slots
		}

		return str(summary)

	def can_be_added(self):
		return len(self.parking_slots) + 1 <= self.floor_size 

	def add_slot(self, vehicle_type):
		if not self.can_be_added():
			return "Floor capacity reached"

		fetch_latest_slot_num = (self.parking_slots[-1]).slot_num if len(self.parking_slots) > 0 else 0
		new_slot = ParkingSlot(vehicle_type, fetch_latest_slot_num + 1, self.floor_num)

		self.parking_slots.append(new_slot)

		return "Successfully added parking slot : {}".format(str(new_slot))

	def remove_slot(self, slot_num):
		pass 


	def search_slot_to_book(self, vehicle_type):
		for slot in self.parking_slots :
			if slot.vehicle_type == vehicle_type and slot.is_available()  :
				return slot 
		return None 

	def search_slot(self, slot_num):
		for slot in self.parking_slots :
			if slot.slot_num == slot_num :
				return slot

		return None 


class Ticket:
	def __init__(self, floor_num, slot_num, parkinglot_id):
		self.floor_num = floor_num
		self.slot_num = slot_num 
		self.parkinglot_id = parkinglot_id

	def __str__(self):
		return "{}_{}_{}".format(self.parkinglot_id, self.floor_num, self.slot_num)

class ParkingLot:
	def __init__(self, Id, N):
		self.Id = Id 
		self.parking_floors = []
		self.capacity = N 

	def can_be_added(self):
		return len(self.parking_floors) + 1 <= self.capacity

	def add_floor(self, floor_num, floor_size):
		if not self.can_be_added() :
			return "Lot capacity reached"

		new_floor = ParkingFloor(floor_num, floor_size)
		self.parking_floors.append(new_floor)
		return "Successfully added parking floor : {}".format(str(new_floor))

	def search_floor(self, floor_num):
		for floor in self.parking_floors :
			if floor.floor_num == floor_num :
				return floor

		return None 


	def add_parking_slot(self, floor_num, vehicle_type):
		found_floor = None 
		for floor in self.parking_floors :
			if floor_num == floor.floor_num :
				found_floor = floor
				break 

		if not found_floor :
			return "Cannot find floor with floor number {}".format(floor_num)


		if not found_floor.can_be_added():
			return "Cannot add parking slot to floor, capacity reached"

		return found_floor.add_slot(vehicle_type)


	def book_slot_and_park(self, vehicle):
		found_slot = None 
		for floor in self.parking_floors :
			found_slot = floor.search_slot_to_book(vehicle.vehicle_type)
			if not found_slot :
				continue 
			else :
				break

		found_slot.add_vehicle(vehicle)
		parking_ticket = Ticket(found_slot.floor_num, found_slot.slot_num, self.Id)

		return "Booked Slot and generated ticket : {}".format(str(parking_ticket))

	def unpark_vehicle(self, ticket):
		lot_id, floor_num, slot_num = ticket.split('_')
		floor = self.search_floor(int(floor_num))
		if not floor :
			return "Bad ticket Id, no such floor".format(floor_num)

		slot = floor.search_slot(int(slot_num))
		if not slot :
			return "Bad ticket Id, no slot {} on floor {}".format(slot_num, floor_num)

		return slot.remove_vehicle()




	def display_free_slots(self, vehicle_type):
		for floor in self.parking_floors :
			print("Floor number {}:".format(floor.floor_num))
			c = 0 
			for slot in floor.parking_slots :
				if slot.vehicle_type == vehicle_type and not slot.can_be_added() :
					print(slot)
					c += 1

			print("Number of Available slots for vehicle type : {}, on floor number : {}, are : {}".format(vehicle_type, floor.floor_num, floor.floor_size - c))

	def display_occupied_slots(self, vehicle_type):
		for floor in self.parking_floors :
			print(floor.floor_num)
			c = 0 
			for slot in floor.parking_slots :
				if slot.vehicle_type == vehicle_type and not slot.can_be_added() :
					print(slot)
					c += 1

			print("Number of occupied slots for vehicle type : {}, on floor number : {}, are : {}".format(vehicle_type, floor.floor_num, c))




vehicle1 = Vehicle(VehicleType.CAR, "ABC123", "Red")
vehicle2 = Vehicle(VehicleType.BIKE, "XYZ789", "Blue")
vehicle3 = Vehicle(VehicleType.TRUCK, "DEF456", "Green")

# Create a parking lot with 2 floors and 10 slots each
parking_lot = ParkingLot(1, 2)
parking_lot.add_floor(1, 10)
parking_lot.add_floor(2, 10)

# Add parking slots to the floors
parking_lot.add_parking_slot(1, VehicleType.CAR)
parking_lot.add_parking_slot(1, VehicleType.BIKE)
parking_lot.add_parking_slot(2, VehicleType.TRUCK)


# Test booking a slot and parking a vehicle
print(parking_lot.book_slot_and_park(vehicle1))
print(parking_lot.book_slot_and_park(vehicle2))
print(parking_lot.book_slot_and_park(vehicle3))

# Test displaying free and occupied slots
parking_lot.display_free_slots(VehicleType.CAR)
parking_lot.display_occupied_slots(VehicleType.TRUCK)
parking_lot.display_free_slots(VehicleType.TRUCK)

# Test unparking a vehicle
ticket_to_unpark = "1_1_1"  # Example ticket for unparking
print(parking_lot.unpark_vehicle(ticket_to_unpark))

parking_lot.display_free_slots(VehicleType.CAR)


ticket_to_unpark = "1_2_3"
print(parking_lot.unpark_vehicle(ticket_to_unpark))

parking_lot.display_free_slots(VehicleType.TRUCK)

