def study_schedule(permanence_period, target_time):
    """Faça o código aqui."""
    if target_time is None:
        return None
    try:
        max_count = sum(
            1 for entry, exit in permanence_period
            if entry <= target_time <= exit
        )

        return max_count
    except TypeError:
        return None
