/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strslen.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: achiu-au <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/02/16 01:18:39 by achiu-au          #+#    #+#             */
/*   Updated: 2019/02/16 01:18:40 by achiu-au         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int		ft_strslen(char *str, char *s)
{
	int		len;

	len = 0;
	while (*str)
	{
		if (!ft_isintab(s, *str))
			len++;
		str++;
	}
	return (len);
}