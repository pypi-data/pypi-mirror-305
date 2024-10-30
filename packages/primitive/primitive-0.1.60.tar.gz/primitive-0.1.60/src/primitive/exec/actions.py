import typing

if typing.TYPE_CHECKING:
    pass


from primitive.utils.actions import BaseAction


class Exec(BaseAction):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def execute_command(self, hardware_identifier: str, command: str) -> None:
        hardware = self.primitive.hardware.get_hardware_from_slug_or_id(
            hardware_identifier=hardware_identifier
        )

        # since we found hardware, we need to check that the user:
        # - has a valid reservation on it
        # - OR if the device is free we can reserve it

        # if we create a reservation on behalf of the user, we need to release it after
        created_reservation_on_behalf_of_user = False

        if active_reservation := hardware["activeReservation"]:
            active_reservation_id = active_reservation["id"]
            reservation_result = self.primitive.reservations.get_reservation(
                reservation_id=active_reservation_id
            )
            reservation = reservation_result.data["reservation"]
        else:
            reservation_result = self.primitive.reservations.create_reservation(
                requested_hardware_ids=[hardware["id"]],
                reason="Executing command from Primitive CLI",
            )
            reservation = reservation_result.data["reservationCreate"]
            created_reservation_on_behalf_of_user = True

        reservation = self.primitive.reservations.wait_for_reservation_status(
            reservation_id=reservation["id"], desired_status="in_progress"
        )

        print(f"Executing command: {command} on {hardware['name']}")

        if created_reservation_on_behalf_of_user:
            print("Cleaning up reservation.")
            self.primitive.reservations.release_reservation(
                reservation_or_hardware_identifier=reservation["id"]
            )
