#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newnode;
	newnode = (listint_t *) malloc(sizeof(listint_t));
	
	if (newnode == NULL)
	{
		return (NULL);
	}

	newnode->n = number;
	*head = newnode;
	newnode->next = NULL;
	return (newnode);
}
