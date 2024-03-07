#include <stdlib.h>
#include "list.h"

/**
 * add_node_end - Add new node to the end of a double circular linked list
 * @list: pointer to the pointer to the head of the list
 * @str: string to copy into the new node
 *
 * Return: Address of the new node, or NULL on failure
 */
List *add_node_end(List **list, char *str)
{
	List *new_node = malloc(sizeof(List));
	List *last = *list;

	if (new_node == NULL)
		return (NULL);

	new_node->str = strdup(str);
	if (new_node->str == NULL)
	{
		free(new_node);
		return (NULL);
	}

	if (*list == NULL)
	{
		new_node->prev = new_node;
		new_node->next = new_node;
		*list = new_node;
	}
	else
	{
		last = (*list)->prev;
		last->next = new_node;
		new_node->prev = last;
		new_node->next = *list;
		(*list)->prev = new_node;
	}

	return (new_node);
}

/**
 * add_node_begin - Add new node to the beginning of a double linked list
 * @list: pointer to the pointer to the head of the list
 * @str: string to copy into the new node
 *
 * Return: Address of the new node, or NULL on failure
 */
List *add_node_begin(List **list, char *str)
{
	List *new_node = malloc(sizeof(List));

	if (new_node == NULL)
		return (NULL);

	new_node->str = strdup(str);
	if (new_node->str == NULL)
	{
		free(new_node);
		return (NULL);
	}

	if (*list == NULL)
	{
		new_node->prev = new_node;
		new_node->next = new_node;
	}
	else
	{
		new_node->prev = (*list)->prev;
		new_node->next = *list;
		(*list)->prev->next = new_node;
		(*list)->prev = new_node;
	}

	*list = new_node;

	return (new_node);
}
