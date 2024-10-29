from pydantic import EmailStr, TypeAdapter, ValidationError, validate_call
from rich.prompt import Prompt

from sereto.cli.utils import Console
from sereto.models.person import Person, PersonType


@validate_call
def prompt_user_for_person(person_type: PersonType) -> Person:
    """Interactively prompt for a person's details.

    Args:
        person_type: The type of person to prompt for.

    Returns:
        The person as provided by the user.
    """
    name: str | None = Prompt.ask("Name", console=Console(), default=None)
    business_unit: str | None = Prompt.ask("Business unit", console=Console(), default=None)
    while True:
        try:
            e: str | None = Prompt.ask("Email", console=Console(), default=None)
            ta: TypeAdapter[EmailStr] = TypeAdapter(EmailStr)  # hack for mypy
            email: EmailStr | None = ta.validate_python(e) if e is not None else None
            break
        except ValidationError:
            Console().print("[red]Please enter valid email address")
    role: str | None = Prompt.ask("Role", console=Console(), default=None)

    return Person(type=person_type, name=name, business_unit=business_unit, email=email, role=role)
