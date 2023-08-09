#include "lists.h"

/**
 * insert_node - Inserts a num into a sorted singly-linked list.
 * @head: A pointer to the head of the linked list.
 * @number: The number to insert.
 *
 * Return: If the function fails - NULL.
 * Otherwise - a pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *k;

	k = malloc(sizeof(listint_t));
	if (k == NULL)
		return (NULL);
	k->n = number;

	if (node == NULL || node->n >= number)
	{
		k->next = node;
		*head = k;
		return (k);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	k->next = node->next;
	node->next = k;

	return (k);
}
