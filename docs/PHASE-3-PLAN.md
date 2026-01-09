# Phase 3: Agent System Refactoring - Strategic Plan

## Current State Analysis

### Files

- `forge/agents/orchestrator.py` - 705 lines (God class)
- `forge/agents/dispatcher.py` - 354 lines (reasonable)
- **Total:** 1,079 lines

### Problems Identified

#### 1. AgentOrchestrator (705 lines) Violations

- ❌ **Massive God Class** - Does EVERYTHING
- ❌ **Mixed Concerns** - Selection + execution + messaging + learning
- ❌ **No Result Types** - Returns mixed types, raises exceptions
- ❌ **Sync/Async Confusion** - Both paradigms mixed in one class
- ❌ **Hard to Test** - Loads config in constructor
- ❌ **Mutable State** - Task objects mutated throughout

#### 2. Agent Selection Strategy (lines 211-273)

- Hard-coded keyword matching
- No extensibility
- Should be pluggable strategy pattern

#### 3. Task Model (lines 56-83)

- Mutable dataclass
- Business logic mixed with data
- Should be immutable with builders

#### 4. Message Handling (lines 478-572)

- Manual message routing
- No event-driven architecture
- Hard to extend

## Refactoring Strategy

### Target Architecture

```
forge/agents/
├── domain/                           # Domain models (immutable)
│   ├── agent.py                     # Agent, AgentType
│   ├── task.py                      # Task (immutable)
│   └── message.py                   # AgentMessage
│
├── selection/                        # Agent selection strategies
│   ├── base.py                      # SelectionStrategy interface
│   ├── keyword_strategy.py          # Keyword matching (default)
│   └── ml_strategy.py               # ML-based (future)
│
├── execution/                        # Task execution
│   ├── sync_executor.py             # Synchronous execution
│   └── async_executor.py            # Asynchronous execution
│
├── services/                         # Business logic
│   ├── agent_service.py             # Agent management
│   ├── task_service.py              # Task operations
│   └── message_service.py           # Message handling
│
├── orchestrator_refactored.py       # New orchestrator (<200 lines)
└── dispatcher.py                    # Keep as-is (already good)
```

### Principles to Apply

1. **Immutable Domain Models** - Data classes with frozen=True
2. **Strategy Pattern** - Pluggable agent selection
3. **Separation of Concerns** - Sync/async executors separate
4. **Result Types** - All operations return Result[T, E]
5. **Event-Driven** - Message bus for agent communication
6. **Dependency Injection** - All dependencies injected

## Implementation Plan

### Step 1: Extract Domain Models (Immutable)

**Create:**

- `forge/agents/domain/agent.py` - Agent data model
- `forge/agents/domain/task.py` - Immutable Task with builder
- `forge/agents/domain/message.py` - AgentMessage

**Benefits:**

- Pure data (no business logic)
- Immutable (thread-safe)
- Easy to test
- Clear contracts

### Step 2: Extract Selection Strategies

**Create:**

- `forge/agents/selection/base.py` - SelectionStrategy interface
- `forge/agents/selection/keyword_strategy.py` - Current implementation
- `forge/agents/selection/context_strategy.py` - Future enhancement

**Benefits:**

- Open/Closed principle (add strategies without modifying code)
- Testable in isolation
- Easy to A/B test different strategies

### Step 3: Separate Sync/Async Execution

**Create:**

- `forge/agents/execution/base.py` - Executor interface
- `forge/agents/execution/sync_executor.py` - Synchronous tasks
- `forge/agents/execution/async_executor.py` - Asynchronous tasks

**Benefits:**

- Clear separation of concerns
- No async/await confusion
- Easy to test separately

### Step 4: Extract Services

**Create:**

- `forge/agents/services/agent_service.py` - Agent registration, retrieval
- `forge/agents/services/task_service.py` - Task creation, management
- `forge/agents/services/message_service.py` - Message routing

**Benefits:**

- Business logic separated from orchestration
- Reusable services
- Easy to mock for testing

### Step 5: Create Refactored Orchestrator

**Create:**

- `forge/agents/orchestrator_refactored.py` - New orchestrator (<200 lines)

**Responsibilities (ONLY):**

- Coordinate services
- Delegate to strategies and executors
- Route to appropriate components

## Success Criteria

- [ ] Orchestrator < 200 lines
- [ ] All operations return Result types
- [ ] Strategy pattern for agent selection
- [ ] Separate sync/async execution
- [ ] Immutable domain models
- [ ] 80%+ test coverage
- [ ] Zero circular dependencies

## Breaking Changes

**None** - New architecture exists alongside old:

- `orchestrator.py` - Original (deprecated)
- `orchestrator_refactored.py` - New implementation

## Timeline

- **Step 1-2:** 30 minutes (domain + strategies)
- **Step 3:** 20 minutes (executors)
- **Step 4:** 30 minutes (services)
- **Step 5:** 20 minutes (orchestrator)
- **Testing:** 20 minutes
- **Total:** ~2 hours

## Metrics

| Metric | Before | Target | Improvement |
|--------|--------|--------|-------------|
| Orchestrator lines | 705 | <200 | -72% |
| Testability | 0% | 100% | +100% |
| Strategy extensibility | No | Yes | ∞ |
| Result types | 0% | 100% | +100% |
| Immutable models | No | Yes | ✅ |
