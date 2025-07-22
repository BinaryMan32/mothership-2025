from mkdocs_macros.plugin import MacrosPlugin

def define_env(env: MacrosPlugin):
    """
    This is the hook for the variables, macros and filters.
    """

    COIN_ICON = ':fontawesome-solid-coins:{ .coin }'

    @env.macro
    def coin(amount):
        return f'`{amount}`{COIN_ICON}'

    HEAT_ICON = ':fire:'

    @env.macro
    def heat(amount):
        return f'`{amount}`{HEAT_ICON}'

    def tier_icon(amount):
        return f':fontawesome-solid-trophy:{{ .tier{amount} }}'

    @env.macro
    def tier(amount):
        return f'`{amount}`{tier_icon(amount)}'

    @env.macro
    def experience(amount):
        return f'`{amount}`:scroll:'

    @env.macro
    def reputation(amount):
        return f'`{amount}`:material-sword-cross:'

    @env.macro
    def stress(amount):
        return f'`{amount}`:fontawesome-solid-heart-crack:'

    def d6_roll_internal(number):
        if 1 <= number <= 6:
            return f'`{number}`:material-dice-{number}:'
        else:
            return f'`{number}`:game_die:'

    def d6_roll_outcome(number):
        if number == 6:
            return 'full'
        if number in (4, 5):
            return 'partial'
        if number in (1, 2, 3):
            return 'bad'

    def d6_rolls_outcome(numbers, result):
        if numbers.count(6) >= 2:
            return 'critical'
        else:
            return d6_roll_outcome(result)

    def outcome_text(outcome):
        if outcome == 'critical':
            return 'Critical Success'
        elif outcome == 'full':
            return 'Full Success'
        elif outcome == 'partial':
            return 'Partial Success'
        elif outcome == 'bad':
            return 'Bad Outcome'

    OUTCOME_ICON = ':fontawesome-solid-font-awesome:'

    def outcome_label(outcome):
        text = outcome_text(outcome)
        return f'{OUTCOME_ICON}{{ .outcome-{outcome} }} {text}'

    @env.macro
    def d6_roll(number):
        roll = d6_roll_internal(number)
        outcome = outcome_label(d6_roll_outcome(number))
        return f'{roll} {outcome}'

    @env.macro
    def d6_rolls(numbers, lowest=False, outcome=True):
        op, extra = (min, '(lowest) ') if lowest else (max, '')
        result = op(numbers)
        rolls = [d6_roll_internal(n) for n in numbers]
        outcome = outcome_label(d6_rolls_outcome(numbers, result))
        return f'[{", ".join(rolls)}] `=` {extra}{d6_roll_internal(result)} {outcome}'

    def character_link(character):
        return f'[{character["name"]}]({character["url"]})'

    def inject_character_links(characters):
        for c in characters.values():
            c['link'] = character_link(c)

    def inject_links(variables):
        inject_character_links(variables.characters)

    inject_links(env.variables)
