import ten99policy

# You can configure the environment for 1099Policy API (sandbox|production)
ten99policy.environment = "sandbox"


# -----------------------------------------------------------------------------------*/
# Updating a contractor (replace xxx with an existing contractor id)
# -----------------------------------------------------------------------------------*/

resource = ten99policy.Contractors.modify(
    "cn_9jwixoKTwa",
    email="john.doe@gmail.com",
    first_name="George",
)
