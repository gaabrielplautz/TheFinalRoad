from code.Entity import Entity
from code.Npc import Npc


class EntityMediator:

    @staticmethod
    #Verica se o Npc atingiu o limite da tela
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, Npc):
            if ent.rect.right < 0:
                ent.health = 0
        pass

    @staticmethod
    #Metodo para verificar colisões
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            teste_entity = entity_list[i]
            EntityMediator.__verify_collision_window(teste_entity)

    @staticmethod
    #Remove o Npc se a vida for menor ou igual a 0
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0:
                entity_list.remove(ent)