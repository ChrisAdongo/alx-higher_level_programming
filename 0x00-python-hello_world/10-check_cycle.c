#include "lists.h"

/**
 * check_cycle - checks if linked list has a cycle
 * @list: linked list to check
 *
 * Return: 1 if the list has a cycle, Otherwise 0 if it doesn't
 */
int check_cycle(listint_t *list)
{
	listint_t *j = list;
	listint_t *k = list;

	if (!list)
	{
		return (0);
	}

	while (j && k && k->next)
	{
		j = j->next;
		k = k->next->next;

		if (j == k)
		{
			return (1);
		}
	}

	return (0);
}
