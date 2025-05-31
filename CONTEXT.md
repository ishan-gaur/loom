# Development Context & Preferences

## Working Style Preferences

### Incremental Changes
- Make small, focused changes rather than large rewrites
- Allow for course correction without waiting for large text generation
- Break complex tasks into discrete, reviewable steps
- Commit changes frequently with clear, descriptive messages

### Communication Style
- Be direct and concise in explanations
- Focus on actionable next steps
- Ask clarifying questions when requirements are ambiguous
- Provide options when multiple approaches are viable

## Project-Specific Guidelines

### Loom Development
- Prioritize voice-first design principles in all decisions
- Document pain points and limitations as they're discovered
- Test with real voice input early and often
- Maintain modular architecture for easy component swapping

### Code Quality
- Write self-documenting code with clear variable names
- Include inline comments for complex voice processing logic
- Implement comprehensive error handling for voice input failures
- Design for accessibility and different speech patterns

### Documentation
- Update relevant docs with each significant change
- Include examples of voice commands and expected behaviors
- Document known limitations and workarounds
- Keep README and setup instructions current

## Technical Preferences

### Architecture Decisions
- Favor local processing over cloud dependencies when possible
- Design for offline functionality where feasible
- Use established libraries and frameworks over custom solutions
- Plan for cross-platform compatibility from the start

### Development Tools
- Use git with descriptive commit messages
- Implement automated testing for critical voice processing paths
- Set up CI/CD for consistent builds across platforms
- Use linting and formatting tools consistently

### Performance Considerations
- Optimize for low-latency voice response
- Monitor memory usage during long voice sessions
- Cache frequently used models and data
- Profile voice processing pipeline regularly

## Research & Experimentation

### Data Collection
- Log voice command success/failure rates
- Track user interaction patterns
- Document edge cases and unusual voice inputs
- Measure latency across different components

### Iteration Process
- Test individual components in isolation
- Gather user feedback early and often
- Validate assumptions with real usage data
- Be prepared to pivot based on discovered limitations

## Communication Protocols

### Status Updates
- Clearly indicate when tasks are complete
- Highlight any blockers or dependencies
- Suggest next logical steps
- Ask for feedback on direction changes

### Problem Solving
- Break down complex issues into smaller parts
- Propose multiple solution approaches when relevant
- Explain trade-offs between different options
- Seek input before making significant architectural decisions