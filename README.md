# ansible_test

This repository validates an ephemeral Ansible workflow.

The test workflow:

1. Clones this repository into a temporary VPS directory.
2. Runs a local Ansible playbook from the temporary checkout.
3. Executes a Python program.
4. Displays the result.
5. Deletes the entire cloned repository afterward.
