#include "lists.h"

/**
 * insert_node - inserting a number into sorted linked list
 * @head: header of the linked list
 * @number: number to insert
 *
 * Return: if fails return NULL otherwise pointer to new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node, *new;

	node = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (node == NULL || node->n >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	new->next = node->next;
	node->next = new;

	return (new);
}
