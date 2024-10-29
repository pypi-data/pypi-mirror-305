/*
 * Copyright (C) 2023 Dominik Drexler and Simon Stahlberg
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program. If not, see <https://www.gnu.org/licenses/>.
 */

#include "mimir/languages/description_logics/grammar.hpp"

#include "mimir/formalism/domain.hpp"
#include "mimir/formalism/predicate.hpp"
#include "parser.hpp"

namespace mimir::dl::grammar
{

VariadicGrammarConstructorFactory create_default_variadic_grammar_constructor_factory()
{
    return VariadicGrammarConstructorFactory(NonTerminalFactory<Concept>(),
                                             ChoiceFactory<Concept>(),
                                             DerivationRuleFactory<Concept>(),
                                             ConceptPredicateStateFactory<Static>(),
                                             ConceptPredicateStateFactory<Fluent>(),
                                             ConceptPredicateStateFactory<Derived>(),
                                             ConceptPredicateGoalFactory<Static>(),
                                             ConceptPredicateGoalFactory<Fluent>(),
                                             ConceptPredicateGoalFactory<Derived>(),
                                             ConceptAndFactory(),
                                             NonTerminalFactory<Role>(),
                                             ChoiceFactory<Role>(),
                                             DerivationRuleFactory<Role>(),
                                             RolePredicateStateFactory<Static>(),
                                             RolePredicateStateFactory<Fluent>(),
                                             RolePredicateStateFactory<Derived>(),
                                             RolePredicateGoalFactory<Static>(),
                                             RolePredicateGoalFactory<Fluent>(),
                                             RolePredicateGoalFactory<Derived>(),
                                             RoleAndFactory());
}

/**
 * Grammar
 */

Grammar::Grammar(std::string bnf_description, Domain domain) : m_grammar_constructor_repos(create_default_variadic_grammar_constructor_factory())
{
    const auto [concept_rules, role_rules] = parse(bnf_description, domain, m_grammar_constructor_repos);
    m_concept_rules = std::move(concept_rules);
    m_role_rules = std::move(role_rules);
}

bool Grammar::test_match(dl::Constructor<Concept> constructor) const
{
    return std::any_of(m_concept_rules.begin(), m_concept_rules.end(), [&constructor](const auto& rule) { return rule->test_match(constructor); });
}

bool Grammar::test_match(dl::Constructor<Role> constructor) const
{
    return std::any_of(m_role_rules.begin(), m_role_rules.end(), [&constructor](const auto& rule) { return rule->test_match(constructor); });
}

const DerivationRuleList<Concept>& Grammar::get_concept_rules() const { return m_concept_rules; }

const DerivationRuleList<Role>& Grammar::get_role_rules() const { return m_role_rules; }

}
