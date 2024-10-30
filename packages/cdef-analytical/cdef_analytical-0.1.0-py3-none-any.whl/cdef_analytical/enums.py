from enum import Enum


class DataCategories(str, Enum):
    # Roles
    ROLE_CHILD = "child"
    ROLE_MOTHER = "mother"
    ROLE_FATHER = "father"

    # Diagnosis Groups
    DIAG_BLOOD_DISORDERS = "blood_disorders"
    DIAG_IMMUNE_SYSTEM = "immune_system"
    DIAG_ENDOCRINE = "endocrine"
    DIAG_NEUROLOGICAL = "neurological"
    DIAG_CARDIOVASCULAR = "cardiovascular"
    DIAG_RESPIRATORY = "respiratory"
    DIAG_GASTROINTESTINAL = "gastrointestinal"
    DIAG_MUSCULOSKELETAL = "musculoskeletal"
    DIAG_RENAL = "renal"
    DIAG_CONGENITAL = "congenital"

    @classmethod
    def roles(cls) -> list[str]:
        """Get all role values."""
        return [member.value for member in cls if member.name.startswith("ROLE_")]

    @classmethod
    def diagnosis_groups(cls) -> list[str]:
        """Get all diagnosis group values."""
        return [member.value for member in cls if member.name.startswith("DIAG_")]
