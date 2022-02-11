global_cost_per_unit = 533
amount_due = 0

def invoice_billing(total_units_required):
    local_unit_price = total_units_required * global_cost_per_unit
    # global_cost_per_unit += local_unit_price thows an error cos pythonw ont let you edit the global var
    return global_cost_per_unit + local_unit_price

print(f"Invoice amount is R{invoice_billing(160)}")
