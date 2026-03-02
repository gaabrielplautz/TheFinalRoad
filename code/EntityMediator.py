#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Entity import Entity
from code.Npc import Npc


class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, Npc):
            if ent.rect.right < 0:
                ent.health = 0

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.__verify_collision_window(entity1)
            for j in range(i + 1, len(entity_list)):
                entity2 = entity_list[j]
                EntityMediator.verify_collision_entity(entity1, entity2)

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list[:]:
            # If life count is <= 0 and it is NOT the Player, remove from the list.
            if ent.health <= 0:
                if ent.__class__.__name__ != 'Player':
                    entity_list.remove(ent)

    @staticmethod
    def verify_collision_entity(ent1: Entity, ent2: Entity):  # REMOVIDO O 'self'
        nome1 = ent1.__class__.__name__
        nome2 = ent2.__class__.__name__

        # Ignore if any of those involved are the fund.
        if 'Background' in nome1 or 'Background' in nome2:
            return False

        # Check if the rectangles are actually touching.
        if ent1.rect.colliderect(ent2.rect):
            # Logic for Player and NPC
            if (nome1 == 'Player' and 'Npc' in nome2) or (nome2 == 'Player' and 'Npc' in nome1):
                ent1.health = 0
                ent2.health = 0
                return True
        return False
