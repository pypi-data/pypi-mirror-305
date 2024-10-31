from typing import Any

def print_info(label: str ="INFO", data: Any =None) -> None:
    """
    Print a formatted message to the console for visual clarity.

    Args:
        label (str, optional): A label for the message, centered and surrounded by dashes. Defaults to 'Label'.
        data: The data to be printed. Can be of any type. Defaults to None.
    """
    
    print(f"\n\n{label:-^50}\n {data} \n{'//':-^50}\n\n")