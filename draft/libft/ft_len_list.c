/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_len_list.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: achiu-au <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/02/16 01:08:45 by achiu-au          #+#    #+#             */
/*   Updated: 2019/02/16 01:09:22 by achiu-au         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int			ft_len_list(t_list *list)
{
	int		len;

	len = 0;
	while (list)
	{
		len++;
		list = list->next;
	}
	return (len);
}
