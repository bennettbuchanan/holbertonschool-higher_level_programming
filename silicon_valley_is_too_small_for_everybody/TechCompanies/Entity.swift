//
//  Entity.swift
//  TechCompanies
//
//  Created by Bennett Buchanan on 6/8/16.
//  Copyright © 2016 Bennett Buchanan. All rights reserved.
//

import UIKit

enum EntityType: String {
    case None, School, TechCompany
}

class Entity {
    var name: String
    var town: String
    var imageName: String
    var type: EntityType
    
    init (name: String, town: String, imageName: String, type: EntityType = .None) {
        self.name = name
        self.town = town
        self.imageName = imageName
        self.type = type
    }
}
